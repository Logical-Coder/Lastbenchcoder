# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:07:04 2021

@author: Praveen Acharya
"""
import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
          'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Z', 'Y', 'Z']
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["!","@","#","$","%","&","*","^"]
print("Welcome to PASSWORD Generator!")
PASSWORD=""
PASSWORD_list=[]
len_letter=int(input("Enter Number of letter should be in PASSWORD:"))
len_number=int(input("Enter Number of Number should be in PASSWORD:"))
len_symbol=int(input("Enter Number of Symbol should be in PASSWORD:"))

for i in range(0,len_letter):
    PASSWORD_list.append(random.choice(letters))
for j in range(0,len_number):
    PASSWORD_list.append(random.choice(numbers))
for k in range(0,len_symbol):
   PASSWORD_list.append(random.choice(symbols))

random.shuffle(PASSWORD_list)
for l in PASSWORD_list:
    PASSWORD+=l
print("Your Strong PASSWORD is=",PASSWORD)
    
    

