#!/usr/bin/env python3
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        return self.__stk[:-1]


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count=0

    def get_counter(self):
        return self.__count

    def pop(self):
        self.__count-=1
        return Stack.pop(self)

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
