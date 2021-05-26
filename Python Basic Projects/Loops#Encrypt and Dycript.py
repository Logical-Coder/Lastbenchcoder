# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:15:49 2021

@author: Brain Hacker
"""
alphbets=['a', 'b','1', 'c','4','#', 'd', 'e', 'f','7','g', 'h', 'i', 'j','5', 'k','6', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v','9', 'w', 'x','3','y', 'z',' ','2','8','0','U', 'C', 'I', 'L', 'H', 'R', 'Z', 'T', 'J', 'W', 'S', 'K', 'F', 'V', 'G', 'N', 'A', 'P', 'E', 'Y', 'X', 'O', 'B', 'D']


def Encript(txt,sft):
    encdtxt=""
    for i in range(0,len(txt)):
        indx=alphbets.index(txt[i])+sft
        if indx>=len(alphbets):
            indx=indx-len(alphbets)
            a=alphbets.copy()
            encdtxt+=a[indx]
        else:
            encdtxt+=alphbets[indx]
    return encdtxt
        
def Decript(txt,sft):
    dcdtxt=""
    for i in range(0,len(txt)):
        indx=alphbets.index(txt[i])-sft
        if indx>=len(alphbets):
            indx=indx-len(alphbets)
            a=alphbets.copy()
            dcdtxt+=a[indx]
        else:
            dcdtxt+=alphbets[indx]
    return dcdtxt
        

text=str(input("Enter Encrypt Message:"))
Shift=int(input("Enter Number of Encript:"))
Encode=Encript(text, Shift)
print("EnCrypted Message:\n",Encode)
dctext=str(input("Enter Dycript Message:"))
dcShift=int(input("Enter Number of Dycript:"))
Dcode=Decript(dctext, dcShift)
print("Decrypted Mesaage :\n",Dcode)
