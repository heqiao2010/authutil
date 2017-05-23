# -*- coding: utf-8 -*-
import unittest
import requests,urllib,json,time,threading
import auth_data

#加上这两个可以不让打印出InsecureRequestWarning警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class test_auth_guding(unittest.TestCase):
      __setupok = 0
      #def setUp(self):
      def test_001_guding(self, esle=None):
            try:
                #-----------------重定向到登录界面------------------------
                def test_guding(thread_name):

                    a=1
                    while a<(auth_data.count+1):

                        date = {
                            'redirect_uri': auth_data.redirect_uri,
                            'usermac':  auth_data.usermac,
                            'userip': auth_data.userip,
                            'userurl': auth_data.userurl,
                            'nas_id': auth_data.nas_id,
                            'ssid': auth_data.ssid
                        }

                        request_redirect_url="http://" + auth_data.portal_host + ":" + auth_data.portal_port + "/portal/protocol?response_type=code&" + urllib.urlencode(date)
                        r = requests.get(request_redirect_url)
                        #----------------------获取templateId-----------------------
                        url_values = urllib.unquote_plus(r.url).split('?')[-1]
                        for key_value in url_values.split('&'):
                            if key_value.split('=')[0]=="templateId":
                                templateId=key_value.split('=')[1]
                                #print "templateId:" +templateId
                                break
                            else:
                                print u'没有获取到templateId'
                                return

                        # ----------------------从portal服务器获取code-----------------------
                        payload= {
                            '_ts': time.ctime(time.time()),
                            'location':'null',
                            'nas_id': auth_data.nas_id,
                            'operateType':7,
                            'redirect_uri':urllib.quote(auth_data.redirect_uri),
                            'signature':urllib.quote(auth_data.password),
                            'ssid':urllib.quote(auth_data.ssid),
                            'templateId':templateId,
                            'userName':urllib.quote(auth_data.username),
                            'userip':urllib.quote(auth_data.userip),
                            'usermac':urllib.quote(auth_data.usermac),
                            'userurl':urllib.quote(auth_data.userurl)
                        }
                        r2=requests.post('http://' + auth_data.portal_host + ':' + auth_data.portal_port + '/portal/login', payload)

                        # ----------------------获取code-----------------------
                        url_values2= urllib.unquote_plus(r2.content).split('?')[-1]
                        for key_value2 in url_values2.split('&'):
                            if key_value2.split('=')[0]=="code":
                                url_code=key_value2.split('=')[1]
                                break
                            elif json.loads(r2.content)['error']:
                                print u'上线失败:'+json.loads(r2.content)['error']
                                return

                        # ----------------------从portal服务器获取accesstoken_url-----------------------
                        accesstoken_url='http://' + auth_data.portal_host + ':' + auth_data.portal_port + '/portal/protocol?response_type=access_token&usermac=' + auth_data.usermac + '&userip=' + auth_data.userip + '&code=' + url_code
                        r3=requests.get(accesstoken_url)
                        access_token=json.loads(r3.content)['access_token']
                        expire_in=json.loads(r3.content)['expire_in']

                        # ----------------------从portal服务器获取用户信息-----------------------
                        userinfo_url="http://" + auth_data.portal_host + ":" + auth_data.portal_port + "/portal/protocol?response_type=userinfo&access_token=" + str(access_token)
                        r4=requests.get(userinfo_url)
                        username = json.loads(r4.content)['username']
                        #print r4.content
                        if username != 0:
                            print thread_name+u',用户：'+username+u',上线成功！'+u'，次数：'+str(a)
                        else:
                            print u'上线失败'
                        a=a+1

                #try:
                    #thread.start_new_thread(test_guding, ('Thread-1', ))
                    #test_guding("Thread-1")
                #except  Exception, err:
                 #   print "error is %s" % err

                class myThread(threading.Thread):  # 继承父类threading.Thread
                    def __init__(self, threadID, name):
                        threading.Thread.__init__(self)
                        self.threadID = threadID
                        self.name = name

                    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
                        test_guding(self.name)
                #根据auth_data设定的参数创建指定的进程数
                b=1
                while b<(auth_data.threads+1):
                    thread1 = myThread(1, "Thread-"+str(b))
                    thread1.start()
                    b=b+1
            except Exception, err:
                  print "error is %s" % err

if __name__ == "__main__":
      # headers = lvfunc.oasislogin()
      unittest.main()

