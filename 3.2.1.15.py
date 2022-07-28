#!/usr/bin/env python3
class QueueError(Exception):  
    pass


class Queue:
    def __init__(self):
        self.que=[]

    def put(self, elem):
        self.que.insert(0,elem)


    def get(self):
        val=self.que[-1]
        self.que=self.que[:-1]
        return val

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
