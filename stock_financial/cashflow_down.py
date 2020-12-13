"""
获取现金流信息

使用示例（获取2018年二季度现金流量数据）：
report_date = time_last_day_of_month(year=2018, month=6)

cash_flow = CashflowRun(
    data_queue='cashflow_data_queue',
    page_queue='cashflow_page_queue',
    crawl_num=10,
    parser_num=10
)

cash_flow.run(report_date=report_date)
"""

from data_urls import *
from comm_funcs import *
import json
import time
import pandas as pd


class CashflowRun(HeyRun):
    def get_down_url(self, **kwargs):
        '''
        实现获取下载链接的接口
        :param kwargs:
        :return:
        '''
        return get_cashflow_url(**kwargs)

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
            'cce_add',
            'cce_add_ratio',
            'netcash_operate',
            'netcash_operate_ratio',
            'netcash_invest',
            'netcash_invest_ratio',
            'netcash_finance',
            'netcash_finance_ratio',
            'sales_services',
            'sales_services_ratio',
            'pay_staff_cash',
            'psc_ratio',
            'receive_invest_income',
            'rii_ratio',
            'construct_long_asset',
            'cla_ratio'
        ]

    def data_parser(self):
        '''
        实现解析数据接口
        :return:
        '''
        redis_client = get_redis_client()
        engine = get_db_engine_for_pandas()
        columns = self.colunm()

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

                try:
                    df = pd.DataFrame(insert_values, columns=columns)

                    df.set_index('report_date', inplace=True)
                    df.fillna(0, inplace=True)

                    df.to_sql(
                        name='s_cashflows',
                        con=engine,
                        if_exists='append')

                    time.sleep(1)
                except Exception as e:
                    except_handle(e)
            except Exception as e:
                except_handle(e)


if __name__ == '__main__':
    report_date = time_last_day_of_month(year=2018, month=6)

    cash_flow = CashflowRun(
        data_queue='cashflow_data_queue',
        page_queue='cashflow_page_queue',
        crawl_num=10,
        parser_num=10
    )

    cash_flow.run(report_date=report_date)
