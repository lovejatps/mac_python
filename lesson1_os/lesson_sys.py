#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年10月23日

@author: huxiaoning
'''
import sys,time
from findertools import sleep


##重定向print输出到文档中。
class __redirection__:
    
    def __init__(self):
        self.f_handler = open("out.log","a")
        sys.stdout = self.f_handler
        self.ISOTIMEFORMAT="%Y-%m-%d %X"
        
    def log(self,valer):
        #self.f_handler.write(valer)
        print time.strftime(self.ISOTIMEFORMAT, time.localtime( time.time() ) ) , valer


def test_sys():
    print dir(sys)
    print sys.platform   ####返回操作系统平台
    print sys.argv[0]    ###返回本程序的完成路径加名字
    #print sys.path
    


if __name__ == '__main__':
    log = __redirection__()
    for i in range(10):
        log.log("huxingning test log! ")
  #  test_sys()
    sys.exit(0)   ##退出程序
    
    
    
    
    
    