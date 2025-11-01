
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

a = pd.read_csv("C:/Users/julia/OneDrive/Documents/programming lab 6/wdi_wide.csv")
a['GNI per capita'] = a['GNI'] / a['Population']
#Part 4
#1
#I can't find a way to facet them. (I tried to use concat but couldn't figure it out)
plt.figure(figsize=(10, 8))
#female
sns.relplot(data = a,
            x="Life expectancy, female", 
            y="GNI per capita", 
            kind="scatter")

plt.figure(figsize=(10, 8))

#Male
sns.relplot(data = a,
            x="Life expectancy, male", 
            y="GNI per capita", 
            kind="scatter"  )
#there does seem to be a pattern were more GNI per capita is better for life expectancy

#B
#female
plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Life expectancy, female", 
            y="GNI per capita",
            hue="Region",
            kind="scatter",)
#Male

plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Life expectancy, male", 
            y="GNI per capita", 
            hue="Region",
            kind="scatter"
            
        )
#it seems like location has similar impact on life expectancy to GNI per captita

#3
#Generate a the plot from item 2, now using lines along with standard deviation. 
#Why can't you see the area representing a standard deviation in the plot?


plt.figure(figsize=(10, 10))
sns.relplot(data = a,
            x="Life expectancy, male", 
            y="GNI per capita", 
            hue="Region",
            kind="line",
            errorbar="sd",
            )
#can't see the standard deviation area beacuse there is no deviation. Need multiple y values

#4
plt.figure(figsize=(10, 10))
sns.lmplot(data = a,
            x="Life expectancy, male", 
            y="GNI per capita", 
            hue="Region",)

