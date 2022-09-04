# -*- coding: utf-8 -*-
"""Data analyst test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17VZo-lUYxNt46kwL4pAK3J8qTXPUkyLe
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
!pip install streamlit

df= pd.read_csv("/content/Assignment-Business-Quant.csv")
df

df = df.sort_values(by=['Item', 'Year','Category'], ascending=[ True, True, True,])
df.head()

df = df.reset_index(drop=True)

Sales_Last_Year=[]
sales_growth=[]

for i in range(df.shape[0]):
  #print(df.iloc[i][2],df.iloc[i-1][3])
  Year = df.iloc[i][2]
  z = df.iloc[i][4]

  if Year== df.Year.min():
     Sales_Last_Year.append(0)
     sales_growth.append(0)
  else:
    x= df.iloc[i-1][3]
    Sales_Last_Year.append(x)
    yy = ((df.iloc[i][3]/x)-1)*100
    sales_growth.append(yy)
    

  
df["Sales Last Year"]= Sales_Last_Year
df["Sales Growth %"]= sales_growth 
df

import streamlit as st
df1 = df['Item'].unique()
Item = df['Item'].drop_duplicates()
make_choice = st.sidebar.selectbox('Select your Item:', Item)

df["Item"]= make_choice

st.write('Item:', make_choice)

