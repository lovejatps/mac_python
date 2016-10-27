#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年10月23日

@author: huxiaoning
'''
import sys
from findertools import sleep
from logtest import Logs


def test_sys():
    print dir(sys)
    print sys.platform   ####返回操作系统平台
    print sys.argv[0]    ###返回本程序的完成路径加名字
    #print sys.path
    


if __name__ == '__main__':
    log = Logs()
    for i in range(10):
        log.log("huxingning test log! ")
  #  test_sys()
    sys.exit(0)   ##退出程序
    
    
    
    
    
    