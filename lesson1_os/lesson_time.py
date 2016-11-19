#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年10月26日

@author: huxiaoning
'''
import time 

def gettime():
    #返回当前时间的时间戳
    print time.time()
    #将当前时间戳转换为当前时区的struct_time
    print time.localtime()
    #返回进程时间
    print time.clock()
    #把一个表示时间的元组表示为这种形式：Sat Dec 14 11:12;26 2013
    print time.asctime()
    #按我们指定的要求格式输出时间
    print time.strftime("%Y-%m-%d %X",time.localtime())
    
    print time.localtime().tm_year  #年
    print time.localtime().tm_mon   #月
    print time.localtime().tm_mday   #日
    print time.localtime().tm_hour    #小时
    print time.localtime().tm_min     #分钟
    print time.localtime().tm_sec      #秒
    print time.localtime().tm_wday     #周 0~6  (0是周日，依此类推)
    print time.localtime().tm_yday      #一年中第几天
    print time.localtime().tm_isdst     #夏令制

    
    
if __name__ == '__main__':
    gettime()
    