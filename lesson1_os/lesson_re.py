#!/usr/bin/env python
#coding=utf-8

'''
Created on 2016年10月25日
@author: huxiaoning
'''
import re 
from logtest import Logs

class Test_re(object):
    
    def __init__(self):
        self.strs ="huxiaoning@163.com"
        self.text = "JGood is a handsome boy, he is cool, clever, and so on..."
        #self.logr = Logs()
        

###re.match 尝试从字符串的开始匹配一个模式，
   
    def testmatch(self):
       m = re.match(r"\u+", self.strs)
       if m :
           print "输入的Email合法" ,m.group(0)
       else:
           print "输入的非法的Email" 
           
           
#re.search函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回，如果字符串没有匹配，则返回None。  
#re.match与re.search的区别：re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，
#函数返回None；而re.search匹配整个字符串，直到找到一个匹配。 
    def getsearch(self):
        m = re.search(r"\shan(ds)ome\s", self.text) 
        if m :
           print "匹配到" ,m.group(0)
        else:
           print  "没有匹配到" 
        msr = re.search(r"\@.+\.", self.strs)
        if msr :
           print "匹配到" ,msr.group(0)
        else:
           print  "没有匹配到" 

#e.sub用于替换字符串中的匹配项。下面一个例子将字符串中的空格 ' ' 替换成 '-' :
#第四个参数指替换个数。默认为0，表示每个匹配项都替换。  
    def testsub(self):
        print re.sub(r" ", "-", self.text,0)   
        
#re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表。
    def getsplit(self):
        m = re.split(r" ", self.text) 
        for str in m:
            print str

#match和search。match是从字符串的起点开始做匹配，而search（perl默认）是从字符串做任意匹配。
    def getmatch(self):
        patterm = re.compile("hu")
        m = patterm.match(self.strs)
        print m.group(0)
           
if __name__ == '__main__':
    Test_re().testmatch()
    Test_re().getsearch()
    Test_re().testsub()
    Test_re().getsplit()
    Test_re().getmatch()
           
