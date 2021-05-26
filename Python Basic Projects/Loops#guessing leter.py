# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:40:20 2021

@author: Praveen Acharya
"""
import random
qwords=[]
show=""
words=["Hangarien","Hellicopter","Soil","Wrong","Plane","science"]
choosed_word=random.choice(words).lower()
for k in choosed_word:
    qwords.append(k)
qwords[random.randint(0, len(qwords)-1)]=" "
index=0
for i in range(0,len(qwords)):
    show+=qwords[i]
    if qwords[i]==" ":
        index=i
print(show)
g=0
while g<5:
    guess=str(input("Guess the blank letter:")).lower()
    if choosed_word[index]==guess:
        print("You got Correct Answer the word it is",choosed_word)
        break
    else:
        g+=1
        print("You Entered wrong letter")
        if g==5:
            print("The Correct letter was",choosed_word[index],"it is'",choosed_word,"'")
        



        
        