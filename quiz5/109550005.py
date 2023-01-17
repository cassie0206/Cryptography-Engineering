# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 12:44:16 2022

@author: ｃａｓｓｉｅ
"""

import hashlib
import binascii


#find the hash value
def hashMD5(n):
    hashVal=hashlib.md5(bytes.fromhex(n))
    return hashVal.hexdigest()[:4]

    

num=input()
num=hashMD5(num)

#find another one that its first four bits MD5 hash value are the same with the input's
val=21267647932558656008062602462446642046

while(1):
    val=hex(val)[2:]
    if num==hashMD5(val):
        print(num,val)
        break
    
    val=int(val,16)
    val+=1



