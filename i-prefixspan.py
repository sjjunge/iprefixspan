
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

    
    
 ### Sequences satisfied with minimum support.

tst=[]
for n in range(0,len(Alpha)):
    AlphaPersonalList=Alpha[n][1]
    for x in range(0,len(AlphaPersonalList)):
        tst.append(AlphaPersonalList[x][0])
        
import collections
SeqSatisfied_1= list(set([x for x in tst if tst.count(x) > 2]))




### PROJECT DB ( S, a1| all tuples )

OneLengthProjectedDB={}
for i in range(0,len(SeqSatisfied_1)):
    temlist=[]
    for j in range(0,len(Alpha)):
        AlphaPersonalList=Alpha[j][1]
        diseaselist=[]
        for k in range(0,len(AlphaPersonalList)):
            if  SeqSatisfied_1[i] == AlphaPersonalList[k][0]:
                for l in range(k+1,len(AlphaPersonalList)):
                    diseaselist.append(AlphaPersonalList[l])
        if(len(diseaselist)>0):
            temlist.append([Alpha[j][0],diseaselist])
    OneLengthProjectedDB.update({SeqSatisfied_1[i]:temlist})

    
    
### MAKING PREFIX (a, YearDifference, b)

ConstructTable={}
for i in range(0,len(OneLengthProjectedDB.keys())):
    temlist=[]
    for j in range(0,len(Alpha)):
        AlphaPersonalList=Alpha[j][1]
        diseaselist=[]
        for k in range(0,len(AlphaPersonalList)):
            if  SeqSatisfied_1[i] == AlphaPersonalList[k][0]:
                for l in range(k+1,len(AlphaPersonalList)):
                    YearDifference=AlphaPersonalList[l][1]-AlphaPersonalList[k][1]
                    diseaselist.append((AlphaPersonalList[k][0],YearDifference,AlphaPersonalList[l][0]))
        if(len(diseaselist)>0):
            temlist.append([Alpha[j][0],diseaselist])
    ConstructTable.update({SeqSatisfied_1[i]:temlist})
    
    
    
    
