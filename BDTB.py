#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 10:32
# @Author  : NooneLiu
# @File    : test.py
# @Desc    :

import urllib2
from bs4 import BeautifulSoup
import re
#
class BDTB():
    def __init__(self, baseUrl, seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = 'see_lz=' + str(seeLZ)

    def getPage(self, pageNum):
        try:
            url = self.baseUrl + '?' + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u'百度贴吧连接失败，错误原因：', e.reason
                return None

    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num".*?><span.*?</span>.*?<span class="red">(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            return None


baseUrl = 'https://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1)
bdtb.getPageNum()
