import requests
import re
import time
import random

class FilmSkySpider(object):
    def __init__(self):
        """定义常用变量"""
        # 一级页面url地址
        self.one_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    def get_html(self,url):
        """功能函数1 - 获取响应内容"""
        # 通过网站查看网页源码,查看网站charset='gb2312'
        # 如果遇到解码错误,识别不了一些字符,则 ignore 忽略掉
        html = requests.get(url=url,headers=self.headers).content.decode('gb2312','ignore')

        return html

    def re_func(self,re_bds,html):
        """功能函数2 - 正则解析功能"""
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)

        return r_list

    def parse_html(self,one_url):
        """开始进行数据抓取"""
        one_html = self.get_html(one_url)
        one_regex = r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        # href: ['/html/xxx','/html/xxx','/html/xxx']
        href_list = self.re_func(one_regex,one_html)

        for href in href_list:
            # 依次遍历每个电影链接,遍历1个,抓取1个
            two_url = 'https://www.dytt8.net' + href
            self.parse_two_page(two_url)
            # uniform: 浮点数,爬取1个电影信息后sleep
            time.sleep(random.uniform(1, 3))

    def parse_two_page(self,two_url):
        """二级页面解析函数,抓取1个电影的详细数据"""
        item = {}
        two_html = self.get_html(two_url)
        two_regex = r'<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
        # two_page_list: [('名称1','ftp://xxxx.mkv')]
        name_href_list = self.re_func(two_regex,two_html)
        # 具体提取数据,名称+下载链接,最好加 try 语句,防止特殊数据
        try:
          item['name'] = name_href_list[0][0].strip()
          item['download'] = name_href_list[0][1].strip()
          print(item)
        except Exception as e:
          print('特殊数据,抛出异常',e)

    def run(self):
        for page in range(1,201):
            url = self.one_url.format(page)
            self.parse_html(url)
            # uniform: 浮点数
            time.sleep(random.uniform(1,3))

if __name__ == '__main__':
    spider = FilmSkySpider()
    spider.run()