#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年10月28日
序列
@author: huxiaoning
'''

if __name__ == '__main__':
    edhan = ["adhan tom",20]
    Jom = ["Jom tom",21]
    database = [edhan,Jom]
    print database
    for data in database:
        print data[0],data[1]
    strname = "hello word!"
    ####索引
    print len(strname)
    print strname[-2]
    print strname[2]
    ####分片
    tap = '<a hraf="http://www.python.org">Python Web Site</a>'
    print tap[9:30]
    print tap[32:-4]
    number = [1,2,3,4,5,6,7,8,9,10]
    print number[3:6]
    print number[0:1]
    print number[:8]
    print number[-3:]
    print number[:10:2]  ##最后的“：2”表示是步长，默认的时候步长为1 
    print number[::-2]  ## 步长为负数时表示从后向前
    print number[::-1]  ##最快的方式把序列倒过来显示出来
    print 9 in number  ### 在序列中查找某个值是否存在 如果存在返回ture 不存在返回false
    print max(number)   ### 查找序列中最大的值，并返回
    print min(number)  ## 查划序列中最小的值，并返回
     
    pass




