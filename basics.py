# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:11:23 2020

@author: Feligx
"""

#LOPA=list of possible aminoacids

def create_LOPA():
    txt=open("lopa.txt","r")
    LOPAtxt=[]
    LOPA_=txt.readlines()
    txt.seek(0)
    for i in range (len(LOPA_)):
        LOPA=txt.readline()
        LOPA=LOPA.rstrip("\n")
        LOPAtxt.append(LOPA)
    return LOPAtxt


def Aminoacids ():
    codons=create_LOPA()
    aminoacid_dict={}
    for i in codons:
        cod1=open(i, "r", encoding="utf8")
        aminoacid=[]
        phe_=cod1.readlines()
        cod1.seek(0)
        for i in range(len(phe_)):
            cod2=cod1.readline()
            cod2=cod2.rstrip("\n")
            aminoacid.append(cod2)
            aminoacid_dict[aminoacid[0]]=aminoacid[1:]
    print(aminoacid_dict)
    #print (aminoacid)
#def Dict_codons ():
    
print(Aminoacids())
