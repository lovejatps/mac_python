#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年10月23日

@author: huxiaoning
'''
import os 

def os_cd_path():
    cwd = os.getcwd()  #保存当前目录地址到cwd变量中
    print cwd
    filepath ="/Users/huxiaoning/Downloads"
#判断目录是否存在 如果存在的话删除
#     listfiles = os.listdir(filepath)
#     for listfile in listfiles:
#         if "huxx" == listfile:
#             os.rmdir(filepath+os.sep+listfile) 
    ####或者另一种方法判断目录是否存在
   # print os.path.exists(filepath+os.sep+"huxx")
    if os.path.exists(filepath+os.sep+"huxx"):
        os.rmdir(filepath+os.sep+"huxx")
    os.chdir(filepath)  #跳转到指定目录
    os.mkdir("huxx")
    
    cwd2 = os.getcwd()
    print cwd2
    os.chdir(cwd)
    
    
    
    
if __name__ == '__main__':
    os_cd_path()