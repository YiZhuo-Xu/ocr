# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:17:26 2022

@author: meta
"""

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
              'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T','U','V','W', 'X', 'Y', 'Z']
Num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
       ]
import random
data = ''
for i in range(1000):
    a = random.randint(0,1)
    if a==0:
        b=random.randint(0,9)
        data+=Num[b]
    elif a==1:
        b=random.randint(0,23)
        data+=characters[b]
    i+=1
with open("D://cha_num.txt","a") as f:
    f.write(data)
        
print(data)
#np.savetxt('D://cha_num.txt',data,fmt='%s')