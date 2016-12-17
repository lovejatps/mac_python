#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年11月19日
序列
@author: huxiaoning
'''

if __name__ == '__main__':
    a = [1,2,4,5,6,7,8]
    c = [a[:] for j in range(4)]
    b = a * 4
    print c 
    print len(c)
    print b
    print len(b)
    
    d = {}
    d[1,2,3] = "foo"
    d[1,0,3] = "bar"
    d["t"] = "teset"
    print d 
    print d[1, 0, 3]
    print d["t"]
    pass