#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年10月27日

@author: huxiaoning
'''
from test.test_popen import python

if __name__ == '__main__':
    print '字符串!'
    print "测试'li'"
    print '测试"li"'
    a =  'a测度 \'go\''
    b =  'b测度 \'g\\o\' 呵'
    print a+b
    l = [1,2,3,4,5]
    print str(l)
    print repr(str(l))
    name = input("输入你的姓名：")   
    print name 
    name = raw_input("输入你的姓名：")
    print name 
    
    pass