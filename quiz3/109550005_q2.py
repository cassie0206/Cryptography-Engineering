# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:24:11 2022

@author: ｃａｓｓｉｅ
"""

f1=open('message1.txt','r')
f2=open('message2.txt','r')
f3=open('message3.txt','r')

#f_out1=open('109550005_msg1.txt','r')
#f_out2=open('109550005_msg2.txt','r')
#f_out3=open('109550005_msg3.txt','r')

list_psg=['']*3

list_psg[0]=f1.read()
list_psg[1]=f2.read()
list_psg[2]=f3.read()


#print(keyLen3)


f1.close()
f2.close()
f3.close()

#f_out1.close()
#f_out2.close()
#f_out3.close()




charFreq=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]


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


    group=['']*key


    for i in range(len(psg)):
        group[i%key]+=psg[i]
        
    keyWord=''
        
    for i in range(key):
        
        psgFreq=[0]*26
        index=0
        
        for j in range(65,91):
            psgFreq[index]=group[i].count(chr(j))
            index+=1
        
        maxVal=-1
        keep=0
        
        for j in range(1,26):
            total=0
            for k in range(26):
                total+=charFreq[k]*psgFreq[(k+j)%26]
             
            if maxVal<total:
                maxVal=total
                keep=j
        
        keyWord+=chr(65+keep)        
        
    return keyWord

  
            
            
print(function(list_psg[0]))
print(function(list_psg[1]))
print(function(list_psg[2]))


#f_out1=open('109550005_msg1.txt','a')
#f_out2=open('109550005_msg2.txt','a')
#f_out3=open('109550005_msg3.txt','a')


#f_out1.write(function(list_psg[0],keyLen1)+'\n')
#f_out2.write(function(list_psg[1],keyLen1)+'\n')
#f_out3.write(function(list_psg[2],keyLen3)+'\n')





#f_out1.close()
#f_out2.close()
#f_out3.close()