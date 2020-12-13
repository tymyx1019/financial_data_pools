"""
获取资产负债表信息

使用示例（获取2018年4季度资产负债率数据）：
bal_run = BalancesheetsRun(
    data_queue='balancesheet_data_queue',
    page_queue='balancesheet_page_queue')
report_date = time_last_day_of_month(year=2018, month=12)

bal_run.run(report_date=report_date)
"""

import time
import json
import pandas as pd
from data_urls import *
from comm_funcs import *


class BalancesheetsRun(HeyRun):

    def get_down_url(self, **kwargs):
        '''
        重写获取下载链接的方法
        :param kwargs:
        :return:
        '''
        return get_balance_sheets_url(**kwargs)

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
            'report_date',
            'monetaryfunds',
            'monetaryfunds_ratio',
            'accounts_rece',
            'accounts_rece_ratio',
            'inventory',
            'inventory_ratio',
            'total_assets',
            'total_assets_ratio',
            'accounts_payable',
            'accounts_payable_ratio',
            'advance_receivables',
            'advance_receivables_ratio',
            'total_liabilities',
            'total_liab_ratio',
            'debt_asset_ratio',
            'total_equity',
            'total_equity_ratio',
            'fixed_asset',
            'industry_code',
            'industry_name'
        ]

    def data_parser(self):
        '''
        实现解析数据接口
        :return:
        '''
        redis_client = get_redis_client()
        engine = get_db_engine_for_pandas()

        column = self.colunm()
        print('解析数据...')
        while True:
            data = redis_client.lpop(self.data_queue)
            if not data:
                break

            try:
                parse_data_list = json.loads(data)
                data_all = parse_data_list['result']['data']

                insert_values = []
                for row in data_all:
                    data_tmp = tuple(map(lambda x: row[x.upper()], column))
                    insert_values.append(data_tmp)

                if insert_values:
                    df = pd.DataFrame(insert_values, columns=column)
                    df.set_index('report_date', inplace=True)
                    df.fillna(0, inplace=True)
                    df.to_sql(
                        name='s_balance_sheets',
                        con=engine,
                        if_exists='append')
                    time.sleep(1)

            except Exception as e:
                except_handle(e)


if __name__ == '__main__':
    bal_run = BalancesheetsRun(
        data_queue='balancesheet_data_queue',
        page_queue='balancesheet_page_queue',
        crawl_num=10,
        parser_num=10)
    report_date = time_last_day_of_month(year=2018, month=12)

    bal_run.run(report_date=report_date)
    # bal_run.data_parser()
