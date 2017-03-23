# -*- coding: UTF-8 -*-
'''
Created on 2017��3��18��

@author: dkf6498
'''
import ConfigParser
import urllib2
import httplib

def readInit(fileName,param):
    config = ConfigParser.ConfigParser()
    config.readfp(open(fileName))
    return config.get("ZIP",param)
   
def updateDefaut(fileName,param,newparam):
    config = ConfigParser.ConfigParser()
    config.read(fileName)
    config.set("ZIP", param, newparam) #这样md5就从1234变成kingsoft了
    config.write(open(fileName, "r+"))
# 发送get请求
def do_get(authurl, domain):
    conn = httplib.HTTPConnection(domain)
    conn.request(method="GET", url=authurl) 
    response = conn.getresponse()
    return response
    
# 发送post请求
# params {'ServiceCode':'aaaa','b':'bbbbb'}
def do_post(authurl, params):
    req = urllib2.Request(url=authurl, data=params)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print "response is :", res;
    return res

def validateParam(*params):
    passParam = 0
    for param in params:
        if param == '':
            passParam = 1
    return passParam
