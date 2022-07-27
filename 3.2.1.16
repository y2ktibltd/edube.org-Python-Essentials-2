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

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self.que)==0:
            return True
        else:
            return False

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
