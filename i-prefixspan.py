
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
        diseasetup=(int(temp[0]),temp[1]);
        diseaselist.append(diseasetup)
    person.append(diseaselist)
    data.append(person)



