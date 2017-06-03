# -*- coding: UTF-8 -*-

import urllib2
import httplib


# Http工具类
class HttpUtils:
    def __init__(self):
        pass

    # 发送get请求
    @staticmethod
    def do_get(url, domain):
        conn = httplib.HTTPConnection(domain)
        conn.request(method="GET", url=url)
        response = conn.getresponse()
        return response

    # 发送post请求
    @staticmethod
    def do_post(url, data):
        req = urllib2.Request(url=url, data=data)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        return res


# the main!
def main():
    if __name__ == "__main__":
        domain = "oasisauth.h3c.com"
        url = "http://oasisauth.h3c.com/portal"
        response = HttpUtils.do_get(url, domain)
        print response.status

main()
