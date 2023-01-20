# -*- coding: utf-8 -*-
"""SEFA BULUT COLAB

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yk8-ioscY2m3Wca4oXTZsPMkTgqlT5Wi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

table=pd.read_excel("unemployment_rate.xlsx")
table

table.info()

table.describe()

table.duplicated().sum()

table.isnull().sum()

for i in table.select_dtypes(include="object").columns:
  print(table[i].value_counts())

table.columns=table.columns.str.title()
for i in table.select_dtypes(include="object").columns:
  print(table[i].value_counts())

table["Month"]=table["Month"].str.title()
for i in table.select_dtypes(include="object").columns:
  print(table[i].value_counts())

table.isnull().sum()

table["Year"].value_counts()

table["Date"]=table["Date"].fillna(0,limit=1)
print(table["Month"].loc[table["Date"]==0],table["Year"].loc[table["Date"]==0])
table["Date"].loc[table["Date"]==0]=table["Date"].loc[table["Date"]==0]="Feb"+"-"+"2019"
table["Date"]=table["Date"].fillna(1,limit=1)
print(table["Month"].loc[table["Date"]==1],table["Year"].loc[table["Date"]==1])
table["Date"].loc[table["Date"]==1]=table["Date"].loc[table["Date"]==1]="Apr"+"-"+"2011"
table["Date"]=table["Date"].fillna(2,limit=1)
print(table["Month"].loc[table["Date"]==2],table["Year"].loc[table["Date"]==2])
table["Date"].loc[table["Date"]==2]=table["Date"].loc[table["Date"]==2]="Jun"+"-"+"2011"
table["Date"]=table["Date"].fillna(3,limit=1)
print(table["Month"].loc[table["Date"]==3],table["Year"].loc[table["Date"]==3])
table["Date"].loc[table["Date"]==3]=table["Date"].loc[table["Date"]==3]="Jul"+"-"+"2011"
table["Date"]=table["Date"].fillna(4,limit=1)
print(table["Month"].loc[table["Date"]==4],table["Year"].loc[table["Date"]==4])
table["Date"].loc[table["Date"]==4]=table["Date"].loc[table["Date"]==4]="Jul"+"-"+"2018"
table["Date"]=table["Date"].fillna(5,limit=1)
print(table["Month"].loc[table["Date"]==5],table["Year"].loc[table["Date"]==5])
table["Date"].loc[table["Date"]==5]=table["Date"].loc[table["Date"]==5]="Aug"+"-"+"2012"
table["Date"]=table["Date"].fillna(6,limit=1)
print(table["Month"].loc[table["Date"]==6],table["Year"].loc[table["Date"]==6])
table["Date"].loc[table["Date"]==6]=table["Date"].loc[table["Date"]==6]="Sep"+"-"+"2013"
table["Date"]=table["Date"].fillna(7,limit=1)
print(table["Month"].loc[table["Date"]==7],table["Year"].loc[table["Date"]==7])
table["Date"].loc[table["Date"]==7]=table["Date"].loc[table["Date"]==7]="Oct"+"-"+"2017"
table["Date"]=table["Date"].fillna(8,limit=1)
print(table["Month"].loc[table["Date"]==8],table["Year"].loc[table["Date"]==8])
table["Date"].loc[table["Date"]==8]=table["Date"].loc[table["Date"]==8]="Nov"+"-"+"2010"
table["Date"]=table["Date"].fillna(9,limit=1)
print(table["Month"].loc[table["Date"]==9],table["Year"].loc[table["Date"]==9])
table["Date"].loc[table["Date"]==9]=table["Date"].loc[table["Date"]==9]="Nov"+"-"+"2018"
print(table["Date"].tail(55))
#print's are for to see the year and month of the row and changed by hand

table["Year"]=table["Year"].fillna(0,limit=1)
print(table["Date"].loc[table["Year"]==0])
table["Year"].loc[table["Year"]==0]=table["Year"].loc[table["Year"]==0]=2012
table["Year"]=table["Year"].fillna(1,limit=1)
print(table["Date"].loc[table["Year"]==1])
table["Year"].loc[table["Year"]==1]=table["Year"].loc[table["Year"]==1]=2019
table["Year"]=table["Year"].fillna(2,limit=1)
print(table["Date"].loc[table["Year"]==2])
table["Year"].loc[table["Year"]==2]=table["Year"].loc[table["Year"]==2]=2010
table["Year"]=table["Year"].fillna(3,limit=1)
print(table["Date"].loc[table["Year"]==3])
table["Year"].loc[table["Year"]==3]=table["Year"].loc[table["Year"]==3]=2010
table["Year"]=table["Year"].fillna(4,limit=1)
print(table["Date"].loc[table["Year"]==4])
table["Year"].loc[table["Year"]==4]=table["Year"].loc[table["Year"]==4]=2012
table.isnull().sum()

table["Month"]=table["Month"].fillna(0,limit=1)
print(table["Date"].loc[table["Month"]==0])
table["Month"].loc[table["Month"]==0]=table["Month"].loc[table["Month"]==0]="Mar"
table["Month"]=table["Month"].fillna(1,limit=1)
print(table["Date"].loc[table["Month"]==1])
table["Month"].loc[table["Month"]==1]=table["Month"].loc[table["Month"]==1]="Apr"
table["Month"]=table["Month"].fillna(2,limit=1)
print(table["Date"].loc[table["Month"]==2])
table["Month"].loc[table["Month"]==2]=table["Month"].loc[table["Month"]==2]="May"
table["Month"]=table["Month"].fillna(3,limit=1)
print(table["Date"].loc[table["Month"]==3])
table["Month"].loc[table["Month"]==3]=table["Month"].loc[table["Month"]==3]="May"
table["Month"]=table["Month"].fillna(4,limit=1)
print(table["Date"].loc[table["Month"]==4])
table["Month"].loc[table["Month"]==4]=table["Month"].loc[table["Month"]==4]="Jul"
table["Month"]=table["Month"].fillna(5,limit=1)
print(table["Date"].loc[table["Month"]==5])
table["Month"].loc[table["Month"]==5]=table["Month"].loc[table["Month"]==5]="Aug"
table["Month"]=table["Month"].fillna(6,limit=1)
print(table["Date"].loc[table["Month"]==6])
table["Month"].loc[table["Month"]==6]=table["Month"].loc[table["Month"]==6]="Nov"
table["Month"]=table["Month"].fillna(7,limit=1)
print(table["Date"].loc[table["Month"]==7])
table["Month"].loc[table["Month"]==7]=table["Month"].loc[table["Month"]==7]="Nov"
table["Month"]=table["Month"].fillna(8,limit=1)
print(table["Date"].loc[table["Month"]==8])
table["Month"].loc[table["Month"]==8]=table["Month"].loc[table["Month"]==8]="Nov"
table["Month"]=table["Month"].fillna(9,limit=1)
print(table["Date"].loc[table["Month"]==9])
table["Month"].loc[table["Month"]==9]=table["Month"].loc[table["Month"]==9]="Dec"

table_filtered=table[table["Year"]<2030]
table_filtered
table_filtered["Year"].value_counts()
#we did that in order to get rid of 99999 rows in data

table_filtered.head(50)

table_filtered.describe()

table_filtered["Primary_School"]=table_filtered["Primary_School"].fillna(table_filtered["Primary_School"].mean())
table_filtered["High_School"]=table_filtered["High_School"].fillna(table_filtered["High_School"].mean())
table_filtered["Associates_Degree"]=table_filtered["Associates_Degree"].fillna(table_filtered["Associates_Degree"].mean())
table_filtered["Professional_Degree"]=table_filtered["Professional_Degree"].fillna(table_filtered["Professional_Degree"].mean())
table_filtered["White"]=table_filtered["White"].fillna(table_filtered["White"].mean())
table_filtered["Black"]=table_filtered["Black"].fillna(table_filtered["Black"].mean())
table_filtered["Asian"]=table_filtered["Asian"].fillna(table_filtered["Asian"].mean())
table_filtered["Hispanic"]=table_filtered["Hispanic"].fillna(table_filtered["Hispanic"].mean())
table_filtered["Men"]=table_filtered["Men"].fillna(table_filtered["Men"].mean())
table_filtered["Women"]=table_filtered["Women"].fillna(table_filtered["Women"].mean())
table_filtered.describe()
table_filtered.isnull().sum()

fig, axes=plt.subplots(1,4,sharey=True,figsize=(40,10))
sns.set_theme(style="whitegrid")
plt.suptitle("Relationship between years and degree types",fontsize=20,fontweight="bold")
ax0= sns.lineplot(ax=axes[0],data=table_filtered,x=table_filtered["Year"],y=table_filtered["High_School"],color="red")
ax0.set_title("High School Degree",fontsize=15,fontweight="bold")
ax1= sns.lineplot(ax=axes[1],data=table_filtered,x=table_filtered["Year"],y=table_filtered["Primary_School"],color="green")
ax1.set_title("Primary School Degree",fontsize=15,fontweight="bold")
ax2= sns.lineplot(ax=axes[2],data=table_filtered,x=table_filtered["Year"],y=table_filtered["Associates_Degree"],color="orange")
ax2.set_title("Associates Degree",fontsize=15,fontweight="bold")
ax3=sns.lineplot(ax=axes[3],data=table_filtered,x=table_filtered["Year"],y=table_filtered["Professional_Degree"],color="brown")
ax3.set_title("Proffesional Degree",fontsize=15,fontweight="bold")

fig, axes=plt.subplots(1,4,sharey=True,figsize=(40,10))
sns.set_theme(style="whitegrid")
plt.suptitle("Relationship between years and races",fontsize=20,fontweight="bold")
ax0= sns.lineplot(ax=axes[0],data=table_filtered,x=table_filtered["Year"],y=table_filtered["Hispanic"],color="brown")
ax0.set_title("Hispanic",fontsize=15,fontweight="bold")
ax1= sns.lineplot(ax=axes[1],data=table_filtered,x=table_filtered["Year"],y=table_filtered["Asian"],color="orange")
ax1.set_title("Asian",fontsize=15,fontweight="bold")
ax2= sns.lineplot(ax=axes[2],data=table_filtered,x=table_filtered["Year"],y=table_filtered["White"],color="grey")
ax2.set_title("White",fontsize=15,fontweight="bold")
ax3=sns.lineplot(ax=axes[3],data=table_filtered,x=table_filtered["Year"],y=table_filtered["Black"],color="black")
ax3.set_title("Black",fontsize=15,fontweight="bold")

fig, axes=plt.subplots(1,2,sharey=True,figsize=(35,10))
sns.set_theme(style="whitegrid")
plt.suptitle("Relationship between years and gender rate",fontsize=20,fontweight="bold")
ax0= sns.lineplot(ax=axes[0],data=table_filtered,x=table_filtered["Year"],y=table_filtered["Men"],color="blue")
ax0.set_title("Men rate",fontsize=15,fontweight="bold")
ax1= sns.lineplot(ax=axes[1],data=table_filtered,x=table_filtered["Year"],y=table_filtered["Women"],color="purple")
ax1.set_title("Women rate",fontsize=15,fontweight="bold")

fig, axes=plt.subplots(1,4,sharey=True,figsize=(40,10))
sns.set_theme(style="whitegrid")
plt.suptitle("The distrubition of where people graduated",fontsize=20,fontweight="bold")
ax0=sns.boxplot(data=table_filtered,y=table_filtered["High_School"],color="red",ax=axes[0])
ax0.set_title("The mean value of where people graduated from High School",fontsize=15,fontweight="bold")
ax1=sns.boxplot(data=table_filtered,y=table_filtered["Primary_School"],color="green",ax=axes[1])
ax1.set_title("The mean value of where people graduated from Primary School",fontsize=15,fontweight="bold")
ax2=sns.boxplot(data=table_filtered,y=table_filtered["Associates_Degree"],color="orange",ax=axes[2])
ax2.set_title("The mean value of where people graduated from Associates",fontsize=15,fontweight="bold")
ax3=sns.boxplot(data=table_filtered,y=table_filtered["Professional_Degree"],color="brown",ax=axes[3])
ax3.set_title("The mean value of where people graduated from Professional",fontsize=15,fontweight="bold")

sns.barplot(data=table_filtered,y=table_filtered["Month"],x=table_filtered["Women"])
sns.color_palette="bright"

table_filtered_jan=table_filtered["Month"].loc[table["Month"]!="Jan"]

fig, axes=plt.subplots(1,3,figsize=(40,10))
sns.set_theme(style="whitegrid")
plt.suptitle("In winter months, relationship between umenployment rates of men",fontsize=20,fontweight="bold")
ax0= sns.lineplot(ax=axes[0],data=table_filtered["Month"],x=table_filtered["Year"].loc[table_filtered["Month"]=="Dec"],y=table_filtered["Men"].loc[table_filtered["Month"]=="Dec"],color="brown")
ax0.set_title("December",fontsize=15,fontweight="bold")
ax1= sns.lineplot(ax=axes[1],data=table_filtered,x=table_filtered["Year"].loc[table_filtered["Month"]=="Jan"],y=table_filtered["Men"].loc[table_filtered["Month"]=="Jan"],color="orange")
ax1.set_title("Jan",fontsize=15,fontweight="bold")
ax2= sns.lineplot(ax=axes[2],data=table_filtered["Month"],x=table_filtered["Year"].loc[table_filtered["Month"]=="Feb"],y=table_filtered["Men"].loc[table_filtered["Month"]=="Feb"],color="grey")
ax2.set_title("February",fontsize=15,fontweight="bold")