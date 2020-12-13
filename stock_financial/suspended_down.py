"""
获取停牌牌个股信息

使用示例（获取2019-05-01及以后的所有停复牌数据）：
    fd = '2019-05-01'
    sus_run = SuspendedRun(
        data_queue='suspended_data_queue',
        page_queue='suspended_page_queue')
    sus_run.run(fd=fd)
"""

try:
    from data_pools.core.data_urls import *
    from data_pools.core.comm_funcs import *
except:
    from data_urls import *
    from comm_funcs import *
import json
import time

import pandas as pd


class SuspendedRun(HeyRun):
    def get_down_url(self, **kwargs):
        '''
        实现获取下载链接的接口
        :param kwargs:
        :return:
        '''
        return get_suspended_url(**kwargs)

    def get_data_pages(self, **kwargs):
        '''
        实现获取分页数量接口
        :param requests_date:
        :return:
        '''
        url = self.get_down_url(**kwargs)
        return int(get_page_num(url)['pages'])

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

                insert_values = []
                for row in parse_data_list['data']:

                    row_list = row.split(',')

                    tuple_list = tuple(row_list)
                    if len(tuple_list) == 9:
                        insert_values.append(tuple_list)

                columns = [
                    'item_code',
                    'item_name',
                    'begin_datetime',
                    'end_datetime',
                    'suspended_type',
                    'suspended_reasons',
                    'mark_type',
                    'begin_date',
                    'resumption_date'
                ]
                df = pd.DataFrame(insert_values, columns=columns)

                df.set_index('begin_date', inplace=True)
                df.fillna(0, inplace=True)

                df.to_sql(
                    name='s_suspended_items',
                    con=engine,
                    if_exists='append')

                time.sleep(1)
            except Exception as e:
                except_handle(e)


if __name__ == '__main__':
    # 获取当前日期
    #fd = get_current_date()

    fd = '2019-05-01'
    sus_run = SuspendedRun(
        data_queue='suspended_data_queue',
        page_queue='suspended_page_queue')
    sus_run.run(fd=fd)
