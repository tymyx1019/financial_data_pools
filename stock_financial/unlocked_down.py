"""
获取解禁个股信息

使用示例（获取从当前时间到2021-12-10所有解禁股票）：
begin_date = get_current_date()
end_date = '2021-12-10'

unlocked_run = UnlockedRun(
    data_queue='unlocked_data_queue',
    page_queue='unlocked_page_queue'
)
unlocked_run.run(begin_date=begin_date, end_date=end_date)
"""
# o_path = os.path.dirname(os.getcwd())
# sys.path.append(o_path)

import json
import time
from comm_funcs import *
from data_urls import *
import pandas as pd



class UnlockedRun(HeyRun):
    def get_down_url(self, **kwargs):
        '''
        实现获取下载链接的接口
        :param kwargs:
        :return:
        '''
        return get_unlocked_url(**kwargs)

    def get_data_pages(self, **kwargs):
        '''
        实现获取分页数量接口
        :param requests_date:
        :return:
        '''
        url = self.get_down_url(**kwargs)
        return int(get_page_num(url)['pages'])

    def colunm(self):
        return [
            'item_code',
            'item_name',
            'unlocked_time',
            'unlocked_type',
            'circulation_percent',
            'mark_type',
            'total_percent',
            'shareholders_num',
            'unlocked_total',
            'true_unlocked_total',
            'circulation_total',
            'locked_total'
        ]

    def data_parser(self):
        '''
        实现解析数据接口
        :return:
        '''
        redis_client = get_redis_client()
        engine = get_db_engine_for_pandas()

        while True:
            data = redis_client.lpop(self.data_queue)
            if not data:
                break

            try:
                parse_data_list = json.loads(data)
                data_all = parse_data_list['data']
                font_map = parse_data_list['font']['FontMapping']
                fonts = {x['code']: x['value'] for x in font_map}

                insert_values = []
                for row in data_all:
                    data_tmp = []
                    data_tmp.append(row['gpdm'])
                    data_tmp.append(row['sname'])
                    ltsj_date = row['ltsj'].replace('-', '')[0:8]
                    data_tmp.append(ltsj_date)
                    data_tmp.append(row['xsglx'])  # 限售股类型

                    if row['zb'] == '-':
                        data_tmp.append(0)
                    else:
                        data_tmp.append(
                            round(
                                float(
                                    row['zb']) *
                                100,
                                2))  # 占解禁前流通市值比例(%)

                    data_tmp.append(row['mkt'])  # 占解禁前流通市值比例(%)

                    if row['zzb'] == '-':
                        data_tmp.append(0)
                    else:
                        data_tmp.append(
                            round(
                                float(
                                    row['zzb']) *
                                100,
                                2))  # 总占比(%)

                    gpcjjgds = row['gpcjjgds']  # 解禁股东数,需要计算
                    for key, val in fonts.items():
                        gpcjjgds = gpcjjgds.replace(key, str(val))

                    data_tmp.append(gpcjjgds)  # 解禁股东数

                    kjjsl = row['kjjsl']  # 解禁数量（万）
                    for key, val in fonts.items():
                        kjjsl = kjjsl.replace(key, str(val))
                    data_tmp.append(int(float(kjjsl) * 10000))

                    jjsl = row['jjsl']  # 实际解禁数量（万），需要计算
                    for key, val in fonts.items():
                        jjsl = jjsl.replace(key, str(val))
                    data_tmp.append(int(float(jjsl) * 10000))  # 实际解禁数量（万）

                    yltsl = row['yltsl']  # 解禁后 已流通数量，需要计算
                    for key, val in fonts.items():
                        yltsl = yltsl.replace(key, str(val))
                    data_tmp.append(int(float(yltsl) * 10000))  # 解禁后 已流通数量

                    wltsl = row['wltsl']  # 未解禁数量
                    for key, val in fonts.items():
                        wltsl = wltsl.replace(key, str(val))
                    data_tmp.append(int(float(wltsl) * 10000))  # 未解禁数量

                    insert_values.append(tuple(data_tmp))

                columns = self.colunm()
                df = pd.DataFrame(insert_values, columns=columns)

                df.set_index('unlocked_time', inplace=True)
                df.fillna(0, inplace=True)

                df.to_sql(
                    name='s_unlocked_items',
                    con=engine,
                    if_exists='append')

                time.sleep(1)

            except Exception as e:
                except_handle(e)


if __name__ == '__main__':
    # 获取从当前日期后 2021-12-10 的解禁股信息
    begin_date = get_current_date()
    end_date = '2021-12-10'

    unlocked_run = UnlockedRun(
        data_queue='unlocked_data_queue',
        page_queue='unlocked_page_queue'
    )
    unlocked_run.run(begin_date=begin_date, end_date=end_date)
