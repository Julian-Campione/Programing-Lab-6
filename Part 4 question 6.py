# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 17:08:12 2025

@author: julia
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

a = pd.read_csv("C:/Users/julia/OneDrive/Documents/programming lab 6/wdi_wide.csv")
a['GNI per capita'] = a['GNI'] / a['Population']
a['emmisions per capita'] = a['Greenhouse gas emissions'] / a['Population']
#6.1
# Is there any association between Internet use and emissions per capita?
plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            y="emmisions per capita", 
            x="Internet use", 
            kind="scatter")

#There is certainly some corilation between the two. 
#The more emmisions the more internet usage (or vise versa) 



#6.2
#Which are the countries with high emissions? (> 0.03)
 

true = a["Greenhouse gas emissions"] > 0.03
countrieswhokillthe_planet = a[true]

print(countrieswhokillthe_planet["Country Name"]                                                                                                                                     )
#NO LOOPS (:
#and if i put ")" at the end of this print function it gives me an error and I do not know why



#6.3
#c) Is there much variation by region (with respect to high emissions vs Internet use)?
plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            y="emmisions per capita", 
            x="Internet use", 
            hue="Region",
            kind="scatter")
#europe uses a lot of internet and realeases a lot emmissions and the inverse for africa


#6.4
#Do all high income economies have high emissions
a["High Income Economy"] == 1
sns.relplot(data=a,
    x="Internet use",
    y="Greenhouse gas emissions",
    col="High Income Economy",
    kind="scatter",
    height=6,
    aspect=1)
#looking at the y value of each graph we can see that some high income economies have low emmisions