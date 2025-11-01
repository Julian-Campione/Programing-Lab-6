# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 15:22:15 2025

@author: julia
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

a = pd.read_csv("C:/Users/julia/OneDrive/Documents/programming lab 6/wdi_wide.csv")
a['GNI per capita'] = a['GNI'] / a['Population']
    
#5.1 I can't figure out how to turn make this a facet from the data
plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Life expectancy, female", 
            y="Physicians", 
            kind="scatter",
                        )

plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Life expectancy, male", 
            y="Physicians", 
            kind="scatter")
#more doctors = longer life
#5.2
plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Life expectancy, female", 
            y="Women in national parliament", 
            kind="scatter")

plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Life expectancy, male", 
            y="Women in national parliament", 
            kind="scatter")
#woman in parliment do not seem to affect life expectancy
#5.3
plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Life expectancy, female", 
            y="Tertiary education, female", 
            kind="scatter")

plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Life expectancy, male", 
            y="Tertiary education, female", 
            kind="scatter")
#more educated women correlates with better life expectancy for both genders

#5.1.1
#Q1 does more emmission corelate with GNI
plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Greenhouse gas emissions", 
            y="GNI", 
            kind="scatter")
#Q2 do internet use and GNI per capita correlate?
plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Internet use", 
            y="GNI per capita", 
            kind="scatter")
#Q3 does total tertiary education have corilation with GNI
a['total tertiary education'] = a['Tertiary education, male'] + a['Tertiary education, female']
plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="total tertiary education", 
            y="GNI", 
            kind="scatter")
# not much corilation for anything

#Q4 Is tourism and have anything to do with the usage of internet

plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="International tourism", 
            y="Internet use", 
            kind="scatter")
# countries with extremely high tourism seem to have more of a chance of having high internet usage.

#Q5 which region has the most tourism?
plt.figure(figsize=(10, 10))
sns.barplot(
    data=a,
    x="Region",
    y="International tourism",)



