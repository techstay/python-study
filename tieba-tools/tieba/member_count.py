"""
获取单个贴吧所有会员
"""
import pymysql

host = 'localhost'
db_name = 'tieba'
username = 'root'
password = '12345678'


def _get_connection(host, username, password, db_name):
    return pymysql.connect(host=host,
                           user=username,
                           password=password,
                           charset='utf8mb4',
                           db=db_name)


def _create_table(connection):
    '''创建数据库表，不过其实用不到，只是为了记录一下SQL语句'''
    create_table_sql = """
    CREATE TABLE tieba_member(
    username CHAR(255) PRIMARY KEY 
    )  ENGINE = MyISAM;
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_sql)
        connection.commit()


def _insert_table(connection, username):
    '''把数据插入到表中'''
    insert_table_sql = """
    INSERT INTO tieba_member 
    VALUES(%s)"""

    with connection.cursor() as cursor:
        cursor.execute(insert_table_sql, (username,))
        connection.commit()


import urllib.request as request
from bs4 import BeautifulSoup
import re
import tieba.util
import logging
import urllib.parse as parse
import requests

logger = logging.getLogger()

encoding = 'GBK'
tieba_name = 'c语言'
decoded_tieba_name = parse.quote(tieba_name, encoding=encoding)

base_url = f'http://tieba.baidu.com/f/like/furank?kw={decoded_tieba_name}'
connection = _get_connection(host, username, password, db_name)


def _get_total_pages():
    '''获取所有用户页数'''
    global encoding
    content = tieba.util.get_url_content(base_url, encoding=encoding)
    soup = BeautifulSoup(content, 'lxml')
    span = soup.find('span', class_='drl_info_txt_gray')
    user_count = int(span.string)
    logger.info(f'用户共有{user_count}个')

    users_per_page = 20
    import math
    total_pages = math.ceil(user_count / users_per_page)
    logger.info(f'用户共有{total_pages}页')
    return int(total_pages)


def _find_all_users(start_page, end_page):
    global connection
    for i in range(start_page, end_page + 1):
        target_url = f'{base_url}&pn={i}'
        # logger.info(f'正在分析第{i}页')
        html = tieba.util.get_url_content(target_url, encoding=encoding)
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.find_all('tr', class_='drl_list_item')

        for index, tr in enumerate(trs):
            name_link = tr.find('div', class_='drl_item_card').a
            name = name_link.string

            try:
                _insert_table(connection, name)
            except Exception as ex:
                logger.error(f'第{i}页第{index}个用户 {name} 发生异常 {ex}')


def make_parts(total: int, part_count: int):
    count_per_part = total // part_count
    for i in range(1, part_count):
        start = count_per_part * (i - 1) + 1
        end = count_per_part * i
        yield (start, end)

    start = count_per_part * (part_count - 1) + 1
    yield (start, total)


import datetime
from multiprocessing import Process

if __name__ == '__main__':

    total_pages = _get_total_pages()

    processes = []
    for start, end in make_parts(total_pages, 4):
        processes.append(Process(target=_find_all_users, args=(start, end)))

    time1 = datetime.datetime.today()
    for process in processes:
        process.start()

    for process in processes:
        process.join()

    time2 = datetime.datetime.today()
    print(f'开始时间{time1}')
    print(f'结束时间{time2}')
    print(f'用时{time2 - time1}')
