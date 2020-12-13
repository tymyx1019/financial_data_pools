"""
获取财务报表信息

使用示例 （获取2020年二季度数据）
report_date = time_last_day_of_month(year=2020, month=6)

statement_run = StatementsRun(
    data_queue='stat_data_queue',
    page_queue='stat_page_queue'
)
statement_run.run(report_date=report_date)
"""


from data_urls import *
from comm_funcs import *
import json
import time
import pandas as pd


class StatementsRun(HeyRun):
    def get_down_url(self, **kwargs):
        '''
        实现获取下载链接的接口
        :param kwargs:
        :return:
        '''
        return get_statements_url(**kwargs)

    def colunm(self):
        return [
            'security_code',
            'security_name_abbr',
            'notice_date',
            'reportdate',
            'update_date',
            'eitime',
            'basic_eps',
            'bps',
            'weightavg_roe',
            'mgjyxjje',
            'xsmll',
            'ystz',
            'yshz',
            'sjltz',
            'sjlhz',
            'assigndscrpt'
        ]

    def get_data_pages(self, **kwargs):
        '''
        实现获取分页数量接口
        :param requests_date:
        :return:
        '''
        url = self.get_down_url(**kwargs)
        return int(get_page_num(url)['result']['pages'])

    def data_parser(self):
        '''
        实现解析数据接口
        :return:
        '''
        redis_client = get_redis_client()
        engine = get_db_engine_for_pandas()
        columns = self.colunm()

        print('数据解析中')
        while True:
            data = redis_client.lpop(self.data_queue)
            if not data:
                break

            try:
                parse_data_list = json.loads(data)
                data_all = parse_data_list['result']['data']

                insert_values = []
                for row in data_all:
                    insert_values.append(
                        tuple(map(lambda x: row[x.upper()], columns)))

                df = pd.DataFrame(insert_values, columns=columns)

                df.set_index('reportdate', inplace=True)
                df['assigndscrpt'].fillna('', inplace=True)
                df.fillna(0, inplace=True)

                df.to_sql(
                    name='s_financial_statements',
                    con=engine,
                    if_exists='append')

                time.sleep(1)

            except Exception as e:
                except_handle(e)


if __name__ == '__main__':
    # 获取2020年二季度数据
    report_date = time_last_day_of_month(year=2020, month=6)

    statement_run = StatementsRun(
        data_queue='stat_data_queue',
        page_queue='stat_page_queue',
        crawl_num=10,
        parser_num=10
    )
    statement_run.run(report_date=report_date)
