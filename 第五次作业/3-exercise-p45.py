# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
numdata=np.random.randint(10,100,size=(50,7))
data=pd.DataFrame(numdata,index=[np.array(range(1,51))],columns=['a','b','c','d','e','f','g'])
data.to_csv("data.csv",mode='w')
colnames=['flymiles','videogames','icecream','type']
df=pd.read_csv('datingTestSet.csv', sep=',', index_col=None, header=None, names= colnames,skiprows=2)
df=df.dropna()
print(df[:5])
print(df[df['type']=='largeDoses'])