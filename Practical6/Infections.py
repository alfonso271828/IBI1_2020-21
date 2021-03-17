import matplotlib.pyplot as plt
Infections = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924 }#define the dictionary
print (Infections)

labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'#draw a pie chart
sizes = [29862124,11285561,11205972,4360823,4234924]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
