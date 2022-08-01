#!/usr/bin/env python3
class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day):
        if day not in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]:
            raise WeekDayError
        self.day=day

    def __str__(self):
        return self.day 

    def add_days(self, n):
        list=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        x=0
        for i in list:
            if i == self.day:
                break
            x+=1
        for i in range(n):
 #           print(i,"i",end="\t")
 #           print(x,"x")
            if x>6:
                x=0
            x+=1
        self.day=list[x]

    def subtract_days(self, n):
        list=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        x=0
        for i in list:
            if i == self.day:
                break
            x+=1
        for i in range(n):
#            print(i,"i",end="\t")
#            print(x,"x")
            if x<0:
                x=6
            x-=1
        self.day=list[x]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
