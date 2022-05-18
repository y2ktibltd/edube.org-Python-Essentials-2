#!/usr/bin/env python3
def mysplit(strng):
    word=""
    word_list=[]
    for ch in strng:
        if ch.isspace():
            if len(word)>0:
                word_list.append(word)
            word=""
        if not ch.isspace():
            word+=ch
    if len(word)>0:
        word_list.append(word)
    return word_list

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
