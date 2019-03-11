# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:00:04 2019

@author: Mahe
"""

from Apriori import Apriori
#n=int(input())
min_support=int(input("Minimum support\n"))
min_confidence=float(input("Minimum Confidence\n"))
min_length=int(input("Minimum Length of rules \n"))
#    #db=pd.read_csv()
#for ik in range(n):
#    inp=input().split()
#    item.append(inp)

alpha=[]
for i in range(ord('a'),ord('z')+1):
    alpha.append(chr(i))
#import pandas as pd
#import numpy as np
import re
item=[]
item1=[]
file =open('datasetUCI.txt','r')
for l in file:
    l=l[:-1]
    
    l=re.sub("[?\s]",'a',l)
    li=l.split(',')
    for j in li:
        if(j in alpha):
            item1.append(j)
    item.append(item1)
    item1=[]
    


###
#dataset=pd.read_csv("Market_Basket_Optimisation.csv")
#item=[]
#item1=[]
#dataset=dataset.iloc[:].values
##dataset=dataset[:100]
#for i in range(len(dataset)):
#    for j in dataset[i]:
#        if(type(j)==str):
#            item1.append(j)
#    item.append(item1)
#    item1=[]
item=item
y=Apriori(item,min_support,min_confidence,min_length)

    
    