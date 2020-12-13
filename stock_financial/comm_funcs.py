"""
公用函数库/类
"""


import random
import requests
import datetime
from redis import StrictRedis
import pymysql
import json
import time
import calendar
import sqlalchemy
import configparser
import sys
import os
import threading
from abc import ABCMeta, abstractmethod


def ua_random():
    '''
    随机获取一个user-agent
    :return: user-agent
    '''
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]

    return random.choice(user_agent_list)


def requests_get(url):
    """
    利用request模拟一个get请求
    :param url:
    :return:
    """
    header = {
        'user-agent': ua_random()
    }

    data = requests.get(url, header)
    if data.status_code == 200:
        return data.text

    return None


def get_current_date():
    """
    获取当前日期
    :return: str,日期
    """
    return datetime.datetime.now().strftime('%Y-%m-%d')


def except_handle(exception_handle):
    print(exception_handle)


def get_mysql_client():
    """
    获取数据库连接
    :return:
    """
    db_config = {
        'host': get_config('mysql', 'host'),
        'user': get_config('mysql', 'user'),
        'password': get_config('mysql', 'password'),
        'database': get_config('mysql', 'database'),
        'port': int(get_config('mysql', 'port')),
        'charset': get_config('mysql', 'charset'),
    }
    return pymysql.connect(**db_config)


def get_redis_client():
    """
    获取redis连接
    :return:
    """
    redis_host = get_config('redis', 'host')
    redis_port = int(get_config('redis', 'port'))
    redis_queue_db = int(get_config('redis', 'queue_db'))
    redis_passwd = get_config('password', None)
    return StrictRedis(
        host=redis_host,
        port=redis_port,
        db=redis_queue_db,
        password=redis_passwd,
        decode_responses=True)


def get_page_num(url):
    """
    获取分页数量
    :param fd: 日期
    :return: str,分页数量
    """
    try:
        requests_text = requests_get(url)
        return json.loads(requests_text)
    except Exception as e:
        # 传给异常处理函数
        except_handle(e)


def down_thread(data_queue, page_queue):
    """
    下载接口数据并存入队列
    :param page_queue: 待下载的url队列
    :param data_queue: 下载后的内容队列
    :return:
    """
    # redis连接
    redis_client = get_redis_client()

    while True:
        try:
            url = redis_client.lpop(page_queue)
            if not url:
                break

            data = requests_get(url)
            redis_client.rpush(data_queue, data)
            time.sleep(1)
        except Exception as e:
            # 传给异常处理函数
            except_handle(e)


def time_last_day_of_month(year=None, month=None):
    """
    获取当前月的最后一天
    :return:
    """
    if year is None:
        year = datetime.datetime.now().year

    if month is None:
        month = datetime.datetime.now().month

    day = calendar.monthrange(year, month)[1]
    if len(str(month)) == 1:
        month = '0' + str(month)
    return '-'.join([str(year), str(month), str(day)])


def get_db_engine_for_pandas():
    host = get_config('mysql', 'host')
    user = get_config('mysql', 'user')
    password = get_config('mysql', 'password')
    database = get_config('mysql', 'database')
    port = int(get_config('mysql', 'port'))

    cnf = "mysql+pymysql://{}:{}@{}:{}/{}".format(
        user, password, host, port, database)
    return sqlalchemy.create_engine(cnf)


class ConfigParser(configparser.RawConfigParser):
    def __init__(self, **kwargs):
        kwargs['allow_no_value'] = True
        configparser.RawConfigParser.__init__(self, **kwargs)

    def __remove_quotes(self, value):
        quotes = ["'", "\""]
        for quote in quotes:
            if len(value) >= 2 and value[0] == value[-1] == quote:
                return value[1:-1]
        return value

    def get(self, section, option):
        value = configparser.RawConfigParser.get(self, section, option)
        return self.__remove_quotes(value)


class MultiThread(threading.Thread):
    ''' 多线程类, 使用redis作为队列 '''

    def __init__(self, func, data_queue, page_queue=None):
        super().__init__()
        self.func = func
        self.page_queue = page_queue
        self.data_queue = data_queue

    def run(self):
        '''
        重写run方法
        '''
        print('启动线程 {}'.format(self.name))
        self.scheduler()
        print('结束线程 {}'.format(self.name))

    # 任务调度
    def scheduler(self):
        if self.page_queue and len(self.page_queue):
            # 爬虫
            self.func(self.data_queue, self.page_queue)
        else:
            # 解析数据
            self.func(self.data_queue)


def get_config(read_default_group, key, arg=None):
    """
    获取配置值
    :param key:
    :return:
    """
    if arg:
        return arg

    try:
        cfg = ConfigParser()
        if sys.platform.startswith("win"):
            work_path = os.path.dirname(os.path.realpath(__file__))
            read_default_file = os.path.join(work_path, 'conf.ini')
        else:
            read_default_file = "conf.cnf"

        cfg.read(os.path.expanduser(read_default_file))
        return cfg.get(read_default_group, key)
    except Exception:
        return arg


class HeyRun(metaclass=ABCMeta):
    """主程序运行类"""
    def __init__(
            self,
            data_queue='data_queue',
            page_queue='page_queue',
            crawl_num=5,
            parser_num=5):
        '''
        数据下载和数据解析初始化
        :param data_queue: 数据储存的队列名称，默认data_queue
        :param page_queue: 分页链接的队列名称，默认page_queue
        :param crawl_num: 开启接口线程数量，默认5个线程
        :param parser_num: 开启数据解析线程数量，默认5个线程
        '''
        self._page_queue = page_queue
        self._data_queue = data_queue
        self._crawl_num = crawl_num
        self._parser_num = parser_num

    @property
    def page_queue(self):
        return self._page_queue

    @page_queue.setter
    def page_queue(self, page_queue):
        if isinstance(page_queue, str):
            self._page_queue = page_queue
        else:
            raise TypeError('分页队列名称必须为字符串')

    @property
    def data_queue(self):
        return self._data_queue

    @data_queue.setter
    def data_queue(self, data_queue):
        if isinstance(data_queue, str):
            self._data_queue = data_queue
        else:
            raise TypeError('数据队列名称必须为字符串')

    @property
    def crawl_num(self):
        return self._crawl_num

    @crawl_num.setter
    def crawl_num(self, num):
        if isinstance(num, int) and num > 0:
            self._crawl_num = num
        else:
            raise TypeError('下载数据线程数量必须为整数且大于0')

    @property
    def parser_num(self):
        return self._parser_num

    @parser_num.setter
    def parser_num(self, num):
        if isinstance(num, int) and num > 0:
            self._parser_num = num
        else:
            raise TypeError('下载数据线程数量必须为整数且大于0')

    @abstractmethod
    def get_down_url(self):
        ''' 返回的下载链接 '''
        pass

    @abstractmethod
    def data_parser(self):
        '''
        数据解析的主要方法，存入数据库等
        :return:
        '''
        pass

    @abstractmethod
    def get_data_pages(self, **kwargs):
        '''
        获取数据分页数量
        :param kwargs: 参数信息参照data_url各个接口地址参数
        :return:
        '''
        pass

    @abstractmethod
    def colunm(self):
        ''' 需要提取的字段 '''
        pass

    def push_pages_to_queue(self, **kwargs):
        '''
        将分页后的链接接口地址写入队列
        :param kwargs:
        :return:
        '''
        self.pages = self.get_data_pages(**kwargs)
        redis_client = get_redis_client()

        # 任务队列，存放url的队列
        for page in range(1, (self.pages + 1)):
            down_url = self.get_down_url(page=page, **kwargs)
            redis_client.rpush(self.page_queue, down_url)

    def down_run(self, **kwargs):
        self.push_pages_to_queue(**kwargs)

        if self.pages == 0:
            raise ValueError('分页数量为0')

        # 分页数量大于5以上开启多线程,否则没有意义
        if self.pages > 5 and self._crawl_num > 1:

            crawl_threads = []
            for i in range(1, (self._crawl_num + 1)):
                thread = MultiThread(
                    down_thread,
                    self.data_queue,
                    self.page_queue)
                thread.start()
                crawl_threads.append(thread)

            # 结束爬虫线程
            for t in crawl_threads:
                t.join()
        else:
            down_thread(self.data_queue, self.page_queue)

    def parser_run(self):
        '''
        从队列中取出数据并解析数据
        :return:
        '''
        if self.pages == 0:
            raise ValueError('分页数量为0')

        if self.pages > 5 and self._parser_num > 1:
            parser_threads = []
            for i in range(1, (self._crawl_num + 1)):
                thread = threading.Thread(
                    target=self.data_parser, args=())
                thread.start()
                parser_threads.append(thread)

            # 结束数据解析线程
            for t in parser_threads:
                t.join()
        else:
            self.data_parser()

    def run(self, **kwargs):
        '''
        下载数据时，也可以直接运行对象中down_run和parser_run
        这里直接给出两个合并
        :param kwargs:这里的参数是data_url
        :return:
        '''
        # 下载数据到队列中
        self.down_run(**kwargs)

        # 解析队列中的数据，并存入数据库中
        self.parser_run()
