#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016年11月15日

@author: huxiaoning
'''


def py_string():
    x = "hello python"
    s = "The value of s is " + str(x)
    ss = "The value of ss is " + repr(x)
    print "s:" ,s 
    print "ss:" ,ss
    
def py_list():
    names =["jek","lili","ning","meme"]
    print "names len :" ,len(names)
    names.append("object")
    print "append(object)" , names
    names.insert(2, "li")
    print "insert li :",names
    print "names[:2]" ,names[:2]
    print "names[2:]",names[2:]
    print "names[2]", names[2]

class Counter:
    def __init__(self,low,high):
        self.curent = low    
        self.high = high
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.curent > self.high:
            exit()
        else:
            self.curent +=1
            return self.curent -1


if __name__ == "__main__":
    py_string()
    py_list()
    print py_list().__doc__
    
    a = Counter(3,8)
    for c in a :
        print c 
    print "next..."
    