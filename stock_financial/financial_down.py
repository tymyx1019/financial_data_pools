"""
获取财务利润表信息

使用示例（获取2020年第三季度利润）：
report_date = time_last_day_of_month(year=2020, month=9)

fina_run = FinacialRun(
    data_queue='fina_data_queue',
    page_queue='fina_page_queue'
)
fina_run.run(report_date = report_date)
"""

from data_urls import *
from comm_funcs import *
import json
import time
import pandas as pd


class FinacialRun(HeyRun):
    def get_down_url(self, **kwargs):
        '''
        实现获取下载链接的接口
        :param kwargs:
        :return:
        '''
        return get_financial_url(**kwargs)

    def get_data_pages(self, **kwargs):
        '''
        实现获取分页数量接口
        :param requests_date:
        :return:
        '''
        url = self.get_down_url(**kwargs)
        return int(get_page_num(url)['result']['pages'])

    def colunm(self):
        return [
            'security_code',
            'security_name_abbr',
            'notice_date',
            'report_date',
            'parent_netprofit',
            'total_operate_income',
            'operate_cost',
            'operate_expense',
            'operate_expense_ratio',
            'sale_expense',
            'manage_expense',
            'finance_expense',
            'total_operate_cost',
            'operate_profit',
            'income_tax',
            'operate_tax_add',
            'total_profit',
            'operate_profit_ratio',
            'deduct_parent_netprofit',
            'dpn_ratio'
        ]

    def data_parser(self):
        '''
        实现解析数据接口
        :return:
        '''
        redis_client = get_redis_client()
        engine = get_db_engine_for_pandas()
        columns = self.colunm()

        print('开始解析数据')
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

                df.set_index('report_date', inplace=True)
                df.fillna(0, inplace=True)

                df.to_sql(
                    name='s_financial_profits',
                    con=engine,
                    if_exists='append')

                time.sleep(1)
            except Exception as e:
                except_handle(e)


if __name__ == '__main__':
    report_date = time_last_day_of_month(year=2018, month=6)

    fina_run = FinacialRun(
        data_queue='fina_data_queue',
        page_queue='fina_page_queue',
        crawl_num=10,
        parser_num=10
    )
    fina_run.run(report_date=report_date)
