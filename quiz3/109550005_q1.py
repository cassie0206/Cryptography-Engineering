# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:29:29 2022

@author: ｃａｓｓｉｅ
"""

f1=open('message1.txt','r')
f2=open('message2.txt','r')
f3=open('message3.txt','r')

#f_out1=open('109550005_msg1.txt','w')
#f_out2=open('109550005_msg2.txt','w')
#f_out3=open('109550005_msg3.txt','w')


psg1=f1.read()
psg2=f2.read()
psg3=f3.read()


def function(psg):
    
    key=0
    value=10

    for i in range(4,8):
        
        list_psg=['']*i
        ic=0
        index=0
    
        for j in psg:
            list_psg[index%i]+=j
            index+=1
            
        for j in range(i):
            numerator = 0
            for k in range(65,91):
                num=list_psg[j].count(chr(k))
                numerator+=num*(num-1)
            
            total=len(list_psg[j])

            #print(numerator/(total*(total-1)))
            ic+=numerator/(total*(total-1))
        
        #print('hi')
        ic/=i
        
        #print(ic)
        if abs(ic-0.066)<value:
            key=i
            value=abs(ic-0.066)
            
            
    print(key)            
    return key
    

#f_out1.write(str(function(psg1))+'\n')
#f_out2.write(str(function(psg2))+'\n')
#f_out3.write(str(function(psg3))+'\n')
function(psg1)
function(psg2)
function(psg3)


f1.close()
f2.close()
f3.close()

#f_out1.close()
#f_out2.close()
#f_out3.close()