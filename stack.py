# -*- coding: utf-8 -*-
"""
Created on Wed May 02 08:18:18 2018

@author: KarthikG
"""

"""
Description:
    This creates a simple stack data structure with class
"""
class stack:
    def __init__(self):
        self.data=[]
        
    def push(self,item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
        
    def peek(self):
        return self.data[-1]
    
    def isEmpty(self):
        if self.data:
            return -1
        else:
            return 1
    
    def showstack(self):
        print self.data
    
a=stack();
a.isEmpty();
a.push(1);
a.push(20);
a.push(3);
a.push(12);
print 'before popping data in stack'
a.showstack()
print a.pop();
print 'after popping data in stack'
a.showstack()

a.push(15);
print 'before peeking data in stack'
a.showstack()
print a.peek();
a.showstack()
print 'thanks'
