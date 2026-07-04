import numpy as np
import pandas as pd 
df=pd.read_csv("Countries.csv")
# print(df)

'''Preprocessing techniques'''
# print(df.shape)
# print(df.info())
# print(df.describe())
'''questions'''
print(df.columns)
# print(df[df['population']==df['population'].max()]["country"])
# print(df[df['population']==df['population'].max()]["capital_city"])
# print(df[df['population']==df['population'].min()]["capital_city"])
# print(df[df['population']==df['population'].min()]["country"])

# print(df.sort_values(by='democracy_score',ascending=False,inplace=True))
# print(df['country'])
# print(df['region'].unique().count()) problem is that unique is numpy function and count is pandas function 
print(df['region'].value_counts().count())
print(df[df['region'] == "Eastern Europe"][ 'country'])
print(df[df['population'] == df['population'].nlargest(2).iloc[1]]['political_leader'])
# nlargest() give the list so we use iloc[] and take out the index value 1 )

print(df[df['political_leader'].isna()]['country'].count())
'''
def countR(name):
    return name.startswith('R')
# This works because the result is True/False
filtered_df = df[df['country_long'].apply(countR)]
print(filtered_df['country'])

'''
count=0
def countR(txt):
    global count
    if "republic" in txt.lower():
        count+=1
    return txt
df['country_long'].apply(countR)
print(count)

arf_df=df[df['continent']=='Africa']
print()
print(arf_df[arf_df['population']==arf_df['population'].max()]['country'])

