#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年10月24日

@author: huxiaoning
'''
import sys,time

##重定向print输出到文档中。
class Logs(object):
    
    def __init__(self):
        self.f_handler = open("out.log","a")
        sys.stdout = self.f_handler
        self.ISOTIMEFORMAT="%Y-%m-%d %X"
        
    def log(self,valer):
        #self.f_handler.write(valer)
        print time.strftime(self.ISOTIMEFORMAT, time.localtime( time.time() ) ) , valer


