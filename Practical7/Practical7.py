import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(11,11),dpi=70)
plt.figure(1)
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:11:2,0:5]) #all columns, and every second row between (and including) 0 and 10
# “total cases” for all rows corresponding to Afghanistan.
my_rows = [] # define a list storing Booleans indicating which rows should be extracted
total_rows = len(covid_data)
for i in range (total_rows): # scan through all rows and find all the rows with 'location' = 'Afghanistan'
    if covid_data.loc[i,"location"] == "Afghanistan" :
        my_rows.append(True) #if 'location' = 'Afghanistan' in a row, the row should be extracted, denoted by Blooean 'True'.
    else:
        my_rows.append(False)
print(covid_data.loc[my_rows,"total_cases"])
my_rows1 =[] # define a list storing rows where 'location' = 'world'
for i in range (total_rows): #extract all the rows 'location' = 'world' and store it for making graph
    if covid_data.loc[i,"location"] == "World" :
        my_rows1.append(True)
    else:
        my_rows1.append(False)
world_new_cases = covid_data.iloc[my_rows1,2] #extract data of world new cases for calculating mean and median and drawing graphs
world_new_deaths = covid_data.iloc[my_rows1,3] #extract data of world new deaths for drawing graph
#calculate the mean and median of world new cases
np.mean(world_new_cases)
np.median(world_new_cases)
print('mean of world new cases = ',np.mean(world_new_cases))
print('median of world new cases = ',np.median(world_new_cases))
ax1 = plt.subplot(221)
plt.boxplot(world_new_cases,#draw a box plot of world new cases
            vert = True,
            whis=  1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showfliers = True,
            notch = False
            )
plt.title("world new cases")
world_dates = covid_data.iloc[my_rows1,0]#extract world dates for x axis of the plot
ax2 = plt.subplot(222)
plt.plot(world_dates,world_new_cases, 'r+', label = "world new cases") #draw a plot of world new cases
plt.plot(world_dates,world_new_deaths, 'b+', label = "world new deaths") #draw a plot of world new deaths
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90) #adjust the form of x axis
plt.title("world new cases and new deaths")
plt.legend(loc="upper left", # make label
            ncol=1,
            mode="None",
            borderaxespad=0,
            title="legends",
            shadow=False,
            fancybox=True)

plt.xlabel("date")
plt.ylabel("number")

my_rows4 =[] #extract rows with 'location' = 'Japan'
for i in range (total_rows):
    if covid_data.loc[i,"location"] == "Japan" :
        my_rows4.append(True)
    else:
        my_rows4.append(False)
Japan = covid_data.iloc[my_rows4,:]
Japan_total_cases = Japan.loc[:,"total_cases"] # extract total cases of Japan
Japan_total_deaths = Japan.loc[:,"total_deaths"] # extract total deaths of Japan
jw = Japan.loc[:,"date"] # extract 'date' as x axis
ax3 = plt.subplot(223)
plt.plot(jw,Japan_total_cases,'r+',label = 'Japan total cases') #draw a plot of total cases in Japan
plt.plot(jw,Japan_total_deaths,'b+',label = 'Japan total deaths') #draw a plot of total deaths in Japan
plt.title("Total cases and deaths in Japan")
plt.legend(loc="upper left", # make label
            ncol=1,
            mode="None",
            borderaxespad=0,
            title="legends",
            shadow=False,
            fancybox=True)
plt.xlabel("date")
plt.ylabel("number")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()

