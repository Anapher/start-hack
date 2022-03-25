import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('./finaldata.csv')
pd.set_option('display.max_columns', None)
unique_locations = []
for row in df['bp_from']:
    unique_locations.append(row)

unique_locations = set(unique_locations)
unique_locations = list(unique_locations)
print(unique_locations)

LocationList = [('Brig', 'BR'), ('Visp', 'VI'), ('Frutigen', 'FR'), ('Spiez', 'SP'), ('Thun', 'TH'), ('Bern', 'BN'),
                ('Zurich HB', 'ZUE'), ('Zurich Flughafen', 'ZFH'), ('Winterthur', 'W'), ('Frauenfeld', 'FF'),
                ('Wienfelden', 'WF'), ('Amriswil', 'AW'), ('Romanshorn', 'RH')]
dates = []
totalres = []
df = df.sort_values(by=['date'])
print(df)
for row in df['date']:
    counter = 0
    dates.append(row)
    for j in df.loc[(df['date'] == row)]['reserved']:
        counter += j
    totalres.append(counter)

print(dates)
print(totalres)
plt.scatter(dates, totalres)
plt.xlabel("Dates")
plt.ylabel("Total Reservation")
plt.title('Dates/Reservation')
plt.show()
plt.savefig('Dates_Reservation.jpg')
