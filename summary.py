import pandas as pd
import numpy as np
import re

data = pd.read_csv("data.txt","r",delimiter="\t",usecols=["Country","Participants","Duration","Lowest"])
df = data[data['Country']!='ERR']

data.info()

df['Country'] = df['Country'].astype(str)
df['Country'] = df['Country'].apply(lambda x: x.replace('.',''))

df['Participants'] = df['Participants'].fillna(0)
df['Participants'] = df['Participants'].astype(int)

df['Duration'] = df['Duration'].fillna(0)
df['Duration'] = df['Duration'].astype(int)

df['Lowest'] = df['Lowest'].fillna(0)
df['Lowest'] = df['Lowest'].astype(float)

#cost per day
df['CPD'] = df['Lowest'] / df['Duration']

import matplotlib.pyplot as plt
import seaborn as sns

#what is the price distribution?
ax = sns.distplot(df['Lowest'],bins=50)
ax.set_xticks(np.arange(round(df['Lowest'].min()/500.0)*500,math.ceil(df['Lowest'].max()/500.0)*500,500))
plt.xlabel('Lowest Price in USD$')
plt.ylabel('Cumulative %')
plt.title("Price Distribution of Lowest Priced Accomodation (USD) Across All Retreats")
plt.show()

#price distribution for diff countries?
c = df['Country'].unique()
c.sort()
sns.boxplot(x='Lowest',y='Country',data=df,order=c)
plt.xlabel('Lowest Price in USD$')
plt.ylabel('Country')
plt.title("Price Range (of the Cheapest Accomodation Available) in USD Per Country")
plt.show()

#In India, what is the price/duration of stay comparison?
india = df[df['Country']=='India']
sns.lmplot(x='Lowest', y='Duration', data=india,  palette='Set1')
plt.xlabel('Lowest Price in USD$')
plt.ylabel('Duration of Stay (Days)')
plt.title("Duration of Stay VS Price Range (of the Cheapest Accomodation Available) in USD In India")
plt.show()

#Across all retreats, what is the distribution of CPD?
c = df['Country'].unique()
c.sort()
sns.boxplot(x='CPD',y='Country',data=df,order=c)
plt.xlabel('Cost Per Day (CPD) in USD$')
plt.ylabel('Country')
plt.title("Price Range (of the Cost Per Day) in USD Per Country")
plt.show()