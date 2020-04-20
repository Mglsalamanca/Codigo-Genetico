#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:32:25 2020

@author: lovelace
"""
#import basics

def TRANSCRIPTION (x):
    x.upper()
    ARN=""
    BasesN=["A","T","C","G"]
    for i in x:
        if i in BasesN:
           if i == "A":
              ARN=ARN+"U"
           elif i == "T":
              ARN=ARN+"A"
           elif i == "C":
               ARN=ARN+"G"
           elif i == "G":
               ARN=ARN+"C"
           else:
               print("no es una cadena de ADN")
    return ARN

#def TRANSLATE (y):
 #   cod1=open("phe.txt", "r")
  #  phe=[]
   # for i in cod1:
    #    phe += i
myADN=input("ingrese su cadema de ADN (EN MAYÚS): ")
myARN=(TRANSCRIPTION(myADN))
print(TRANSCRIPTION(myADN))