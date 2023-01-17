# -*- coding: utf-8 -*-

"""
I use for-loop to go through the cypher if there is vowel, then mod its index to keep which row
it is in. After that subtract 3.6(7*9) or 2.8(9*7) to get the difference and print the smaller difference
of the dimension. 

"""

sentence="ECDTMECAERAUOOLEDSAMMERNENASSODYTNRVBNLCRLTIQLAETRIGAWEBAAEIHOR"

list1=[0]*7
list2=[0]*9


for i in range(63):
    if sentence[i]=='A' or sentence[i]=='E' or sentence[i]=='I' or sentence[i]=='O' or sentence[i]=='U':
        num=i%7
        list1[num]+=1
        num=i%9
        list2[num]+=1
          

x=0
for i in list1:
   x+=abs(i-3.6)
   

y=0
for i in list2:
    y+=abs(i-2.8)

print('7*9:%f' %x)
print('9*7:%f' %y)
 
if x>y:
    print('Because the sum of diference of 9*7 is less, the dimension is 9*7')
else:
     print('Because the sum of diference of 7*9 is less, the dimension is 7*9')