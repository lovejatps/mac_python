#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年10月28日
列表
@author: huxiaoning
'''

if __name__ == '__main__':
    
    number = [1,2,3,4,5,6,7,8,9,10]
    numberlist = list('Hello word!')
    print numberlist
    numberlist[0]='h'
    print numberlist
    del numberlist[-1]   ###删除列表中的某一个元素
    print numberlist
    numberlist[-3:] = list('11111')  ###分片付值，对列表中的元素进行修改 数量不一样也没问题，列表是可变的
    print numberlist
    numberlist[0:0] = list('huxn')  ###分片付值，对列表中的元素进行进入插入
    print numberlist
    numberlist.insert(0, 'love')
    print numberlist
    print numberlist.pop()   ###在没有参数的时候，取出最后一个元素【且在在列表中移除该元素】,,也可以带参数
    print numberlist
    numberlist.sort()  ### 排序
    print numberlist
    
    pass