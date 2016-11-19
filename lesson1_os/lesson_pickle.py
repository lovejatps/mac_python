#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年10月26日

@author: huxiaoning
'''
from distutils.log import INFO
try:
    import cPickle as pickle
except:
    import pickle
import pprint

class Test_Pickle(object):
   def __init__(self):
        self.info = ['123',4324,'asdfg','apple','fruit','chicken','food','cat','breafast']
        print "原始数据:",self.info
        pprint.pprint(self.info)

   def getPickle(self):
        pickle.dump(self.info,open("path.log","w"),2)   ##序列化数据
        data2 = pickle.load(open("path.log","r"))
        print "反序列化数据：",data2



if __name__ == '__main__':
    tp = Test_Pickle()
    tp.getPickle()
