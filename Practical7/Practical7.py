import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,6),dpi=100)
plt.figure(1)
os.chdir("D:/Content/Introduction to Bioinformatics/Practical")
a = os.getcwd()
b = os.listdir()
print (a)
print (b)
covid_data = pd.read_csv("full_data.csv")
print(covid_data.head(11))
print(covid_data.info())
print(covid_data.describe())
print(covid_data.iloc[0,1])
print(covid_data.iloc[2,0:5],covid_data.iloc[0:2,:],covid_data.iloc[0:10:2,0:5])
# a : b integer from a to b, without b.
# a : b : c integer from a to b with a difference of c.
# : all the rows or columns.
print(covid_data.iloc[0:3,[0,1,3]])
my_columns = [True, True, False, True, False, False]#define which columns to show
print(covid_data.iloc[0:3,my_columns])
print(covid_data.loc[2:4,"date"])

print(covid_data.loc[0:81,"total_cases"])
my_rows = []
total_rows = len(covid_data)
for i in range (total_rows):
    if covid_data.loc[i,"location"] == "Afghanistan" :
        my_rows.append(True)
    else:
        my_rows.append(False)
print(covid_data.loc[my_rows,"total_cases"])
my_rows1 =[]
for i in range (total_rows):
    if covid_data.loc[i,"location"] == "World" :
        my_rows1.append(True)
    else:
        my_rows1.append(False)
world_new_cases = covid_data.iloc[my_rows1,2]
print(world_new_cases)
print(np.mean(world_new_cases))
print(np.median(world_new_cases))
ax1 = plt.subplot(221)
plt.boxplot(world_new_cases,
            vert = True,
            whis=  1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showfliers = True,
            notch = False
            )

world_dates = covid_data.iloc[my_rows1,0]
print(world_dates)
ax2 = plt.subplot(222)
plt.plot(world_dates,world_new_cases, 'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title("world new cases")
plt.xlabel("date")
plt.ylabel("number")


my_rows2 =[]
for i in range (total_rows):
    if covid_data.loc[i,"location"] == "China" :
        my_rows2.append(True)
    else:
        my_rows2.append(False)
        my_rows2 = []
China_new_cases = covid_data.iloc[my_rows2,2]
my_rows3 = []
for i in range (total_rows):
    if covid_data.loc[i,"location"] == "United Kingdom" :
        my_rows3.append(True)
    else:
        my_rows3.append(False)
        my_rows3 = []
United_Kingdom_new_cases = covid_data.iloc[my_rows3,2]

my_rows4 =[]
for i in range (total_rows):
    if covid_data.loc[i,"location"] == "Japan" :
        my_rows4.append(True)
    else:
        my_rows4.append(False)
Japan = covid_data.iloc[my_rows4,:]
print(Japan)
Japan_total_cases = Japan.loc[:,"total_cases"]
Japan_total_deaths = Japan.loc[:,"total_deaths"]
jw = Japan.loc[:,"date"]
ax3 = plt.subplot(223)
plt.plot(jw,Japan_total_cases)
plt.plot(jw,Japan_total_deaths)
plt.title("Total cases and deaths in Japan")
plt.xlabel("date")
plt.ylabel("number")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()

