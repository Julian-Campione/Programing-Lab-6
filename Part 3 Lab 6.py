# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:15:50 2025
Julian Campione (there were an odd number of people in class so im alone)
@author: julia
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#why not import seaborn as cbrn?

#part 3

a = pd.read_csv("C:/Users/julia/OneDrive/Documents/programming lab 6/wdi_wide.csv")
b = a.info()
#there are 217-207= 10 null categories for physicians (10 countries did not report how many physicians they have)
#there are 217-217= 0 null categories for population
print(b)
print("...LLLLL...") #just so i can easily see 
c = a.nunique()
print(c)
#according to this data set there are 5 unique regions.


d = a.describe()
print(d)
#descirbe calculates the count(amount) mean, standard deviation, min, 25% 50% 75% and max of all the columnus

a['GNI per capita'] = a['GNI'] / a['Population']
print(a['GNI per capita'])
print("...LLL...")

e =  a['Region'].value_counts()
print("this is how many countries are in each region:", e)

print("...LLL...")

high_income = a[a['High Income Economy' ] == 1].value_counts()
f = high_income.value_counts()
print("there are:", f, " high income economies")
print(f)

print("...LLL...")

g = pd.crosstab(a['High Income Economy'] == 1, a['Region']).iloc[1]
print("This is the value of high for each region", g)

print("...LLL...")
    
nunber_counrtries = 0
h = a['Life expectancy, female'].dropna()
for h in a['Life expectancy, female']:
    if h >= 80:
        nunber_counrtries += 1
       
        
print("there are", nunber_counrtries, "with a female life expectancy above 80")

