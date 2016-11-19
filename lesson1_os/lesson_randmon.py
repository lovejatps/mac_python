#!/usr/bin/env python 
#coding=utf-8
'''
Created on 2016年10月27日

@author: huxiaoning
'''
import random

class Test_randmon(object):
    def __init__(self):
        self.info = [1,2,3,4,5,6,7,8,9,10]
        self.str ="asdfghjkl"
        
    def get_random(self):
        print "随机0~1的值：",random.random()
        print "random.uniform()正好弥补了上面函数的不足，它可以设定浮点数的范围，一个是上限，一个是下限。:",random.uniform(10,100)
        print "random.randint()随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值",random.randint(10,50)
        print "random.choice()可以从任何序列，比如list列表中，选取一个随机的元素返回",random.choice(self.info)
        print "random.choice()可以从任何序列，比如list列表中，选取一个随机的元素返回",random.choice(self.str)
        print "random.shuffle()如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法。", random.shuffle(self.info)
        print "计算数据几次方:",4**2
        

if __name__ == '__main__':
    trand = Test_randmon()
    trand.get_random()
    