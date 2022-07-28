#!/usr/bin/env python3
class Timer:
    def __init__(self,h=0,m=0,s=0):
        self.__h=h
        self.__m=m
        self.__s=s

    def __str__(self):
        hour=str(self.__h)
        if len(hour)==1:hour="0"+hour
        minute=str(self.__m)
        if len(minute)==1:minute="0"+minute
        second=str(+self.__s)
        if len(second)==1:second="0"+second
        return hour+":"+minute+":"+second

    def next_second(self):
        self.__s+=1
        if self.__s>59:
            self.__s=00
            self.__m+=1
            if self.__m>59:
                self.__m=00
                self.__h+=1
                if self.__h>23:
                    self.__h=00

    def prev_second(self):
        self.__s-=1
        if self.__s<0:
            self.__s=59
            self.__m-=1
            if self.__m<0:
                self.__m=59
                self.__h-=1
                if self.__h<0:
                    self.__h=23

timer = Timer(9, 0, 19)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
