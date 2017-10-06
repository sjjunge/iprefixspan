
import pymssql
import os, sys, string
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

conn = pymssql.connect(server="",
                       user="",
                       password="",
                       database="")
cur = conn.cursor()


cur.execute("select top 20 * from __Grad_7")

data=[]
for rows in cur:
    person=[]
    person.append(rows[0])
    myrow=rows[1].split('),(')
    myrow[0]=myrow[0][1:]
    myrow[len(myrow)-1]=myrow[len(myrow)-1][:-1]
    diseaselist=[]
    for tup in myrow:
        temp=tup.split(',')
        diseasetup=(temp[0],int(temp[1]));
        diseaselist.append(diseasetup)
    person.append(diseaselist)
    data.append(person)


    

 ### Set Minimum Support

Minsup=0.005
    
 ### Sequences satisfied with minimum support.

tst=[]
for n in range(0,len(Alpha)):
    AlphaPersonalList=Alpha[n][1]
    for x in range(0,len(AlphaPersonalList)):
        tst.append(AlphaPersonalList[x][0])
        
import collections
DisListCount=Counter(DisList)
Itemsnum1=sum(DisListCount.values())
DisListCount_Minsup_1={k:v for (k,v) in DisListCount.items() if  v/Itemsnum1 > Minsup}
DisList_Minsup_1=list(DisListCount_Minsup_1.keys())




for i in range(0,len(DisList_Minsup_1)):
    Alpha_Minsup_1=[]
    for j in range(0,len(Alpha)):
        PerList=Alpha[j][1]
        PerDislist=[]
        for k in range(0,len(PerList)):
            if PerList[k][0] in DisList_Minsup_1:
                PerDislist.append(PerList[k])
        if(len(PerDislist)>0):
            Alpha_Minsup_1.append([Alpha[j][0],PerDislist])




 ### PROJECT DB ( S, a1| all tuples )

OneLengthProjectedDB={}
for i in range(0,len(DisList_Minsup_1)):
    temlist=[]
    for j in range(0,len(Alpha_Minsup_1)):
        PerList=Alpha_Minsup_1[j][1]
        diseaselist=[]
        for k in range(0,len(PerList)):
            if  DisList_Minsup_1[i] == PerList[k][0]:
                for l in range(k+1,len(PerList)):
                    diseaselist.append(PerList[l])
        if(len(diseaselist)>0):
            temlist.append([Alpha[j][0],diseaselist])
    OneLengthProjectedDB.update({DisList_Minsup_1[i]:temlist})




### MAKING PREFIX (a, YearDifference, b)

ConstructTable_1={}
for i in range(0,len(OneLengthProjectedDB.keys())):
    temlist=[]
    for j in range(0,len(Alpha_Minsup_1)):
        PerList=Alpha_Minsup_1[j][1]
        diseaselist=[]
        for k in range(0,len(PerList)):
            if  DisList_Minsup_1[i] == PerList[k][0]:
                for l in range(k+1,len(PerList)):
                    YearDifference=PerList[l][1]-PerList[k][1]
                    diseaselist.append((PerList[k][0],YearDifference,PerList[l][0]))
        if(len(diseaselist)>0):
            temlist.append([Alpha[j][0],diseaselist])
    ConstructTable_1.update({DisList_Minsup_1[i]:temlist})




### PREFIX 1 satisfied with minimum support.

ConstructTable_1_vals=tuple(ConstructTable_1.values())
PrefixTemp_1=[]

for n in range(0,len(ConstructTable_1_vals)):
    temp=ConstructTable_1_vals[n]
    # temp2=[]
    for j in range(0,len(temp)):
        PrefixTemp_1.extend(temp[j][1])

PrefixTemp_1_Count=Counter(PrefixTemp_1)
Itemsnum2=sum(PrefixTemp_1_Count.values())
PrefixTemp_1_Count_Minsup_1={k:v for (k,v) in PrefixTemp_1_Count.items() if v/Itemsnum2 > Minsup}





