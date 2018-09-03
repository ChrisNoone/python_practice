# coding:utf-8

import urllib,urllib2
import json
from itertools import count

class outlet_Schedule():
    
    def __init__(self):
        self.cid = "c4f34d75-e411-4295-a302-cd1ecba7d132"
        self.url = self.url()
        self.data = self.data()
        self.headers = self.headers()
        
    def url(self):
        url = "https://smartapitest.vesync.com/v1/mqtt/device/%s/schedule" % self.cid
        return url
    
    def data(self):
        data_file = open(r"D:\body.txt","r")
        '''data_file是list类型'''
        data = ''.join(data_file.readlines())
        '''data是str类型'''
        return data
        
    def headers(self):
        headers = {
            "accountid":"1000058",
            "tk":"98fupz664m3ZhohxwAyQj04uGIUscfS9de35Sby5-v9MqQ==",
            "tz":"Asia/Shanghai"
            }
        return headers
        
    def queryScheduleList(self):
        req = urllib2.Request(self.url,None,self.headers)
        response = urllib2.urlopen(req)
        result = response.read()
        result_json =  json.dumps(json.loads(result),sort_keys=True,indent=2)
        return result_json

    def addSchedule(self):
        req = urllib2.Request(self.url,self.data,self.headers)
        response = urllib2.urlopen(req)
        print "\n"+json.dumps(json.loads(response.read()),sort_keys=True,indent=2)+"\n"
#         
    def editSchedule(self):
        req = urllib2.Request(self.url,self.data,self.headers)
        req.get_method = lambda: 'PUT'
        response = urllib2.urlopen(req)

if __name__ == "__main__":
    '''查询Schedule'''
#     print outlet_Schedule().queryScheduleList()
#     print "Schedule个数：",outlet_Schedule().queryScheduleList().count("event")

    '''添加schedule'''
    print "开始添加..."
    print "计划任务数：%s" % outlet_Schedule().queryScheduleList().count("event")
    schedule2 = outlet_Schedule().addSchedule()
    print "添加结束..."
    print "计划任务数：%s" % outlet_Schedule().queryScheduleList().count("event")

    '''编辑schedule'''
#     outlet_Schedule().editSchedule()