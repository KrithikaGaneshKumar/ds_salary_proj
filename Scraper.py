# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:52:43 2020

@author: Krithika Ganesh
"""
import glassdoor_scraper as gs
import pandas as pd
path= "C:/Users/Krithika Ganesh/Documents/ds_salary_proj/chromedriver.exe"
df= gs.get_jobs('data scientist',1000, False, path,15)
df.to_csv('glassdoor_jobs.csv', index = False)