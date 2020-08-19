# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:12:03 2020

@author: Krithika Ganesh
"""

import pandas as pd
df= pd.read_csv('glassdoor_jobs.csv')
df.columns
#dropping columns 
df=df.drop(['Competitors','Headquarters'], axis=1)
#Agenda
# Parsing Salary 
df= df[df['Salary Estimate']!='-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
df['min_salary']= minus_Kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary']= minus_Kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary']= (df.min_salary+df.max_salary)/2