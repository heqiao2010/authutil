# -*- coding: UTF-8 -*-

import urllib


# 认证工具类
class AuthUtils:
    def __init__(self):
        pass

    # 获取重定向地址
    @staticmethod
    def get_redirect_url(domain, user_mac, user_ip, redirect_uri, user_url, nas_id, ssid):
        url = "http://"
        url += domain + "/portal/protocol?response_type=code"
        url += "&redirect_uri=" + urllib.quote(redirect_uri)
        url += "&usermac=" + urllib.quote(user_mac)
        url += "&userip=" + user_ip
        url += "&userurl=" + urllib.quote(user_url)
        url += "&nas_id=" + str(nas_id)
        url += "&ssid=" + urllib.quote(ssid)
        return url

    # 获取登录页面URL
#     @staticmethod
#     def get_login_page_url():




# the main!
def main():
    if __name__ == "__main__":
        url = AuthUtils.get_redirect_url("oasisauth.h3c.com", "QQ-QQ-QQ-QQ-QQ", "172.12.12.12", "http://www.baidu.com",\
                                   "http://www.baidu.com", 123123, "h3c-lvzhou")
        print "url", url

# test!
main()
