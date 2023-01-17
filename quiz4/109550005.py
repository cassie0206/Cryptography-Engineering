# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 23:47:43 2022

@author: ｃａｓｓｉｅ
"""

sentence="EOEYEGTRNPSECEHHETYHSNGNDDDDETOCRAERAEMHTECSEUSIARWKDRIRNYARANUEYICNTTCEIETUS"

list1=[0]*7
list2=[0]*11


for i in range(77):
    if sentence[i]=='A' or sentence[i]=='E' or sentence[i]=='I' or sentence[i]=='O' or sentence[i]=='U':
        num=i%7
        list1[num]+=1
        num=i%11
        list2[num]+=1
          

x=0
for i in list1:
   x+=abs(i-4.4)
   

y=0
for i in list2:
    y+=abs(i-2.8)

print('7*11:%f' %x)
print('11*7:%f' %y)
 
index=0

if x>y:
    print('Because the sum of diference of 11*7 is less, the dimension is 11*7')
    index=1
else:
     print('Because the sum of diference of 7*11 is less, the dimension is 7*11')
    

     


ref ='WITHM ALICE TOWAR DNONE WITHC HARIT YFORA LLWIT\
HFIRM NESSI NTHER IGHTA SGODG IVESU STOSE ETHER\
IGHTL ETUSS TRIVE ONTOF INISH THEWO RKWEA REINT\
OBIND UPTHE NATIO NSWOU NDSTO CAREF ORHIM WHOSH\
ALLHA VEBOR NETHE BATTL EANDF ORHIS WIDOW ANDHI\
SORPH ANTOD OALLW HICHM AYACH IEVEA NDCHE RISHA\
JUSTA NDLAS TINGP EACEA MONGO URSEL VESAN DWITH\
ALLNA TIONS GREEC EANNO UNCED YESTE RDAYT HEAGR\
AGREE MENTW ITHTR UKEYE NDTHE CYPRU STHAT THEGR\
EEKAN DTURK ISHCO NTING ENTSW HICHA RETOP ARTIC\
IPATE INTHE TRIPA RTITE HEADQ UARTE RSSHA LLCOM\
PRISE RESPE CTIVE LYGRE EKOFF ICERS NONCO MMISS\
IONED OFFIC ERSAN DMENA NDTUR KISHO FFICE RSNON\
COMMI SSION EDOFF ICERS ANDME NTHEP RESID ENTAN\
DVICE PRESI DENTO FTHER EPUBL ICOFC YPRUS ACTIN\
GINAG REEME NTMAY REQUE STTHE GREEK ANDTU RKISH\
GOVER NMENT STOIN CREAS EORRE DUCET HEGRE EKAND\
TURKI SHCON TINGE NTSIT ISAGR EEDTH ATTHE SITES\
OFTHE CANTO NMENT SFORT HEGRE EKAND TURKI SHCON\
TINGE NTSPA RTICI PATIN GINTH ETRIP ARTIT EHEAD\
QUART ERSTH EIRJU RIDIC ALSTA TUSFA CILIT IESAN\
DEXEM PTION SINRE SPECT OFCUS TOMSA NDTAX ESASW\
ELLAS OTHER IMMUN ITIES ANDPR IVILE GESAN DANYO\
THERM ILITA RYAND TECHN ICALQ UESTI ONSCO NCERN\
INGTH EORGA NIZAT IONAN DOPER ATION OFTHE HEADQ\
UARTE RSMEN TIONE DABOV ESHAL LBEDE TERMI NEDBY\
ASPEC IALCO NVENT IONWH ICHSH ALLCO MEINT OFORC\
ENOTL ATERT HANTH ETREA TYOFA LLIAN CE\
'
bigram=[]
bigramFreq=[]
wordTable=[]
frequencyTable=[]

for i in range(65,91):
    for j in range(65,91):
        biword=chr(i)+chr(j)
        binum=ref.count(biword)
        bigram.append(biword)
        bigramFreq.append(binum)
        for k in range(65,91):
            word = chr(i)+chr(j)+chr(k)
            num = ref.count(word)
            if num!=0:
                wordTable.append(word)
                frequencyTable.append(num)

if index==1:        
    list3=['']*7
else:
    list3=['']*11

j=0
                
for i in sentence:
    list3[int(j/11)]+=i
    j+=1


ans=[0]*7
ans[0]=2
ans[1]=5

visit=[False]*7
visit[2]=True
visit[5]=True



for i in range(5):
    maximum=0
    index=0
    for j in range(7): 
        num=0
        plain=list3[ans[i]][0]+list3[ans[i+1]][0]
        base=bigramFreq[bigram.index(plain)]#given frequency
        for k in range(11):
            if base==0:#避免分母為0
                continue
            if visit[j]==False:#還沒被排序的column
                plain+=list3[j][k]#第j column 第k個字          
                if plain in wordTable:#這三個字有在table裡
                    pr=frequencyTable[wordTable.index(plain)]
                    num+=(pr/base)#記錄這一column的conditional probabilty
                if k!=10:
                    plain=list3[ans[i]][k+1]+list3[ans[i+1]][k+1]#換下一row的trigram的前兩個字
                    base=bigramFreq[bigram.index(plain)]
        if maximum<num:#紀錄occrence最高的column
            index=j
            maximum=num
    ans[i+2]=index#把最高occrence的column index記住
    visit[index]=True#以防下次繼續檢查這一column

    
print('\n\n')

cipher=['']*11

for i in range(11):
    for order in ans:
        cipher[i]+=list3[order][i]#根據剛剛紀錄 column order把它用row的形式記住
for i in range(11):
    for word in cipher[i]:#印出plaintext diagram
        print(word,end='')
    print('\n')
