'''
数据来源地址
'''

from functools import partial

from comm_funcs import *


def get_suspended_url(**kwargs):
    '''
    获取停牌复牌的个股信息，来自东方财富网
    :param kwargs:
    :param sty : 'SRB',
    :param st : '2', 排序字段，2：停牌开始时间，6：复牌时间
    :param sr : '-1',排序，-1：倒序
    :param mkt:'1',
    :param fd:开始时间，格式为 '2020-01-06',
    :param page: '1',
    :param psize: '30',
    :param type: 'FD',
    :param js: '{"pages":"(pc)","data":[(x)]}',
    :param time_stamp: int(round(time.time(), 3) * 1000)
    :return: str:url
    '''
    domain = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx'
    param_sty = kwargs.get('sty', 'SRB')
    param_st = kwargs.get('st', '2')
    # 排序
    param_sr = kwargs.get('sr', '-1')
    param_mkt = kwargs.get('mkt', '1')
    param_fd = kwargs.get('fd')
    param_page = kwargs.get('page', '1')
    param_psize = kwargs.get('psize', '30')
    parma_type = kwargs.get('type', 'FD')
    parma_js = kwargs.get('js', '{"pages":"(pc)","data":[(x)]}')
    time_stamp = kwargs.get('time_stamp', int(round(time.time(), 3) * 1000))

    dfp_url = '{}?cb=&type={}&sty={}&st={}&sr={}&mkt={}&fd={}&p={}&pageNo=1&ps={}&js={}&_={}'.format(
        domain,
        parma_type,
        param_sty,
        param_st,
        param_sr,
        param_mkt,
        param_fd,
        param_page,
        param_psize,
        parma_js,
        time_stamp
    )
    return dfp_url


def get_unlocked_url(**kwargs):
    '''
    获取解禁的个股信息，来自东方财富网
    :param kwargs:
    :param sr : '-1',解禁时间排序，-1：解禁时间倒序
    :param page: '1',
    :param psize: '30',
    :param begin_date: 格式为'2020-10-20',默认为当前时间
    :param end_date: 格式为'2020-10-20',默认为开始时间的700天后
    :return: str:url
    '''
    domain = 'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?token=70f12f2f4f091e459a279469fe49eca5&'
    # 排序字段 默认按解禁时间
    param_st = 'ltsj'
    # 排序 1解禁时间由近到远，-1解禁时间由远到近
    param_sr = kwargs.get('sr', '1')
    param_page = kwargs.get('page', '1')
    param_psize = kwargs.get('psize', '30')
    parma_type = 'XSJJ_NJ_PC'
    parma_js = '{"pages":"(tp)","data":(x),"font":(font)}'

    today_date = get_current_date()
    end_date = (
        datetime.datetime.now() +
        datetime.timedelta(
            days=700)).strftime('%Y-%m-%d')

    param_begin_date = kwargs.get('begin_date', today_date)
    param_end_date = kwargs.get('end_date', end_date)
    parma_filter = kwargs.get(
        'filter', '(mkt=)(ltsj>=^{}^ and ltsj<=^{}^)'.format(
            param_begin_date, param_end_date))
    time_rt = kwargs.get('rt', 53529 * 1000 + random.randint(110, 998))

    unlocked_url = '{}st={}&sr={}&p={}&ps={}&type={}&js={}&filter={}&rt={}'.format(
        domain,
        param_st,
        param_sr,
        param_page,
        param_psize,
        parma_type,
        parma_js,
        parma_filter,
        time_rt
    )
    return unlocked_url


def get_financial_url(**kwargs):
    '''
    获取利润表信息，来自东方财富网
    :param kwargs:
    :param st : '2', 排序字段，REPORT_DATE:报道时间
    :param sr : '-1',排序，-1：倒序
    :param page: '1',
    :param psize: '50',
    :param type: 'RPT_DMSK_FN_INCOME',
    :param report_date: 日期，格式为2020-06-31,代表第二季度
    :return: str:url
    '''

    token = '894050c76af8597a853f5b408b759f5d'
    domain = 'http://datacenter.eastmoney.com/api/data/get?callback='
    param_st = kwargs.get('st', 'REPORT_DATE')
    # 排序
    param_sr = kwargs.get('sr', '-1')
    param_psize = kwargs.get('psize', '50')
    param_page = kwargs.get('page', '1')
    parma_type = kwargs.get('type', 'RPT_DMSK_FN_INCOME')
    param_sty = 'ALL'
    report_date = kwargs.get('report_date', time_last_day_of_month())
    param_filter = "(REPORT_DATE='{}')".format(report_date)

    # time_last_day_of_month(year=2020, month=6)

    financial_url = '{}&st={}&sr={}&ps={}&p={}&sty={}&filter=&token={}&type={}&filter={}'.format(
        domain,
        param_st,
        param_sr,
        param_psize,
        param_page,
        param_sty,
        token,
        parma_type,
        param_filter
    )
    return financial_url


def get_statements_url(**kwargs):
    '''
    获取业绩快报信息，来自东方财富网
    主要获取的字段有，每股收益、每股净资产、净资产收益率、每股经营现金流、销售毛利、所处行业
    :param kwargs:
    :param page: '1',分页
    :param psize: '30',每页数量
    :param report_date: 日期，格式为2020-06-31,代表第二季度
    :return: str:url
    '''

    token = '894050c76af8597a853f5b408b759f5d'
    domain = 'http://datacenter.eastmoney.com/api/data/get?callback='
    param_st = 'UPDATE_DATE,SECURITY_CODE'
    # 排序
    param_sr = '-1,-1'
    param_psize = kwargs.get('psize', '50')
    param_page = kwargs.get('page', '1')
    parma_type = 'RPT_LICO_FN_CPD'
    param_sty = 'ALL'
    report_date = kwargs.get('report_date', time_last_day_of_month())

    # (SECURITY_TYPE_CODE+in+("058001001","058001008")):只查询A股，去掉可以查询B股和新三板
    param_filter = "(SECURITY_TYPE_CODE+in+(%22058001001%22%2C%22058001008%22))(REPORTDATE='{}')".format(report_date)

    statements_url = '{}&st={}&sr={}&ps={}&p={}&type={}&sty={}&token={}&filter={}'.format(
        domain,
        param_st,
        param_sr,
        param_psize,
        param_page,
        parma_type,
        param_sty,
        token,
        param_filter
    )
    return statements_url


def get_balance_sheets_url(**kwargs):
    '''
    获取资产负债表信息，来自东方财富网
    :param kwargs:
    :param page: '1',
    :param psize: '50',
    :param report_date: 日期，格式为2020-06-31,代表第二季度
    :return: str:url
    '''
    balance_sheets_url = partial(
        get_financial_url,
        st='NOTICE_DATE,SECURITY_CODE',
        sr='-1,-1',
        type='RPT_DMSK_FN_BALANCE')
    return balance_sheets_url(**kwargs)


def get_cashflow_url(**kwargs):
    '''
    获取现金流数据
    :param kwargs:
    :return:
    '''
    cash_flow_url = partial(
        get_financial_url,
        st='NOTICE_DATE,SECURITY_CODE',
        sr='-1,-1',
        type='RPT_DMSK_FN_CASHFLOW')
    return cash_flow_url(**kwargs)



