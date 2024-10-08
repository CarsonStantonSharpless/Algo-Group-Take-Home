"""Author: Carson Stanton-Shapless"""

# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values

class IntStack:
    def __init__(self,val =None, prev =None):
        self.val = val
        self.prev = prev

    def _push(self,new):
        if self.val:
            temp = IntStack(self.val,self.prev)
            self.val = new
            self.prev = temp
        else:
            self.val = new

    def _pop(self):
        temp =self.val
        if self.prev:
            self.val = self.prev.val
            self.prev = self.prev.prev
        else:
            self.val=None
        return (temp)
    
    def _peek(self):
        return self.val
    
    def _size(self):
        if self.val:
            i =1
            curr = self
            while curr.prev != None:
                i +=1
                curr = curr.prev
            return i
        return 0
