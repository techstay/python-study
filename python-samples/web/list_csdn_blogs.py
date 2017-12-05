import requests
from bs4 import BeautifulSoup
import re
import urllib.parse as parse


class CsdnHelper:
    """登录CSDN和列出所有文章的类"""
    csdn_login_url = 'https://passport.csdn.net/account/login?ref=toolbar'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
    blog_url = 'http://write.blog.csdn.net/postlist/'

    def __init__(self):
        self._session = requests.session()
        self._session.headers = CsdnHelper.headers

    def login(self, username, password):
        '''登录主函数'''
        form_data = self._prepare_login_form_data(username, password)
        response = self._session.post(CsdnHelper.csdn_login_url, data=form_data)
        if 'UserNick' in response.cookies:
            nick = response.cookies['UserNick']
            print(parse.unquote(nick))
        else:
            raise Exception('登录失败')

    def _prepare_login_form_data(self, username, password):
        '''从页面获取参数，准备提交表单'''
        response = self._session.get(CsdnHelper.csdn_login_url)
        login_page = BeautifulSoup(response.text, 'lxml')
        login_form = login_page.find('form', id='fm1')

        lt = login_form.find('input', attrs={'name': 'lt'})['value']
        execution = login_form.find('input', attrs={'name': 'execution'})['value']
        eventId = login_form.find('input', attrs={'name': '_eventId'})['value']
        form = {
            'username': username,
            'password': password,
            'lt': lt,
            'execution': execution,
            '_eventId': eventId
        }

        return form

    def _get_blog_count(self):
        '''获取文章数和页数'''
        response = self._session.get(CsdnHelper.blog_url)
        blog_page = BeautifulSoup(response.text, 'lxml')
        span = blog_page.find('div', class_='page_nav').span
        print(span.string)
        pattern = re.compile(r'(\d+)条\s*共(\d+)页')
        result = pattern.findall(span.string)
        blog_count = int(result[0][0])
        page_count = int(result[0][1])
        return blog_count, page_count

    def print_blogs(self):
        '''输出文章信息'''
        blog_count, page_count = self._get_blog_count()
        for index in range(1, page_count + 1):
            url = f'http://write.blog.csdn.net/postlist/0/0/enabled/{index}'
            response = self._session.get(url)
            page = BeautifulSoup(response.text, 'lxml')
            links = page.find_all('a', href=re.compile(r'http://blog.csdn.net/u011054333/article/details/(\d+)'))
            print(f'----------第{index}页----------')
            for link in links:
                blog_name = link.string
                blog_url = link['href']
                print(f'文章名称:《{blog_name}》 文章链接:{blog_url}')


if __name__ == '__main__':
    csdn_helper = CsdnHelper()
    username = input("请输入用户名")
    password = input("请输入密码")
    csdn_helper.login(username, password)
    csdn_helper.print_blogs()
