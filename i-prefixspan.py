
import pymssql
import pandas as pd
import collections as col
import time
import operator 

### Connect to mssql server 

conn = pymssql.connect(server="",
                       user="",
                       password="",
                       database="")
cur = conn.cursor()


cur.execute("select top 20 * from __Grad_7")

Alpha=[]
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
    Alpha.append(person)


    

 ### Set Minimum Support

Minsup=
transactions_num=


 ### Sequences satisfied with minimum support.

DisList=[]
for n in range(0,len(Alpha)):
    PerList=Alpha[n][1]
    for x in range(0,len(PerList)):
        DisList.append(PerList[x][0])
        


DisListCount=col.Counter(DisList)
DisListCount_Minsup_1={k:v for (k,v) in DisListCount.items() if float(v)/transactions_num > Minsup}
DisList_Minsup_1=list(DisListCount_Minsup_1.keys())

 ### saves the diseases satisfied min_sup 
  
final_data=pd.DataFrame(DisListCount_Minsup_1.items(),columns=['sicks','count'])
final_data.to_csv('first_rules_2002.csv', sep=',', encoding='utf-8')


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
                    diseaselist.append([PerList[k][0],YearDifference,PerList[l][0]])
        if(len(diseaselist)>0):
            temlist.append([Alpha[j][0],diseaselist])
    ConstructTable_1.update({DisList_Minsup_1[i]:temlist})



 ### Making Category ..... the YearDifference
   
ConstructTable_1_list=list(ConstructTable_1.values())
  
    
for i in range(0,len(ConstructTable_1_list)):
    for j in range(0,len(ConstructTable_1_list[i])):
        for k in range(0,len(ConstructTable_1_list[i][j][1])):
            if ConstructTable_1_list[i][j][1][k][1] in [0]:
                ConstructTable_1_list[i][j][1][k][1]=0
            elif ConstructTable_1_list[i][j][1][k][1] in [1,2,3]:
                ConstructTable_1_list[i][j][1][k][1]=1
            elif ConstructTable_1_list[i][j][1][k][1] in [4,5,6]:
                ConstructTable_1_list[i][j][1][k][1]=2
            elif ConstructTable_1_list[i][j][1][k][1] in [7,8,9,10]:
                ConstructTable_1_list[i][j][1][k][1]=3
    
    
    
    
   
### PREFIX 1 satisfied with minimum support.
PrefixTemp_1=[]
for n in range(0,len(ConstructTable_1_list)):
    temp=ConstructTable_1_list[n]
    for j in range(0,len(temp)):
        PrefixTemp_1.extend(temp[j][1])
        
PrefixTemp_1_tup=[tuple(x) for x in PrefixTemp_1]      


PrefixTemp_1_Count=col.Counter(PrefixTemp_1_tup)
PrefixTemp_1_Count_Minsup_1={k:v for (k,v) in PrefixTemp_1_Count.items() if float(v)/transactions_num > Minsup}


 ### save the final data 
  
final_data=pd.DataFrame(PrefixTemp_1_Count_Minsup_1.items(),columns=['sicks','count'])






