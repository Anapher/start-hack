import pandas as pd
import numpy as np

df  = pd.read_csv('./treated_data/train_congestion.csv')
df3 = pd.read_csv('./treated_data/train_congestion831.csv')
df2 = pd.read_csv('finaldata9.csv')
df4 = pd.read_csv('finaldata831.csv')
pd.set_option('display.max_columns', None)
# Data set 1
VI_days = df.loc[df.loc[:,'VI_days_before_last_booking']>0]
#print(VI_days)
dates = []
for i in VI_days['Unnamed: 0']:
    dates.append(i)

y = []
dates_1 = []
times = []
for i in range(len(dates)) :
    time = (df2.loc[ (df2['date'] == dates[i])]['dep_soll'])
    if len(time) > 0 :

        for j in range(len(time)):
            Vi = df.loc[df['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df.loc[df['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap :
                y.append(1)
            else :

                print("VI : ", Vi, " Cap", cap)
                y.append(0)

            dates_1.append(dates[i])
            times.append(time.iloc[j])

print(y)

#data set 2

VI_days1 = df3.loc[df3.loc[:,'VI_days_before_last_booking']>0]
dates = []
for i in VI_days1['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)) :
    time = (df4.loc[(df4['date'] == dates[i])]['dep_soll'])
    if len(time) > 0 :

        for j in range(len(time)):
            Vi = df3.loc[df3['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df3.loc[df3['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:

                print("VI : ", Vi, " Cap", cap)
                y.append(0)

            dates_1.append(dates[i])
            times.append(time.iloc[j])
print(y)
#data set 3
df6 = pd.read_csv('finaldata822.csv')
df5 = pd.read_csv('./treated_data/train_congestion822.csv')
VI_days2 = df5.loc[df5.loc[:, 'VI_days_before_last_booking'] > 0]
dates = []
for i in VI_days2['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)):
    time = (df6.loc[(df6['date'] == dates[i])]['dep_soll'])
    if len(time) > 0:
        for j in range(len(time)):
            Vi = df5.loc[df5['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df5.loc[df5['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:

                print("VI : ", Vi, " Cap", cap)
                y.append(0)

            dates_1.append(dates[i])
            times.append(time.iloc[j])
print(y)
#data set 4
df7 = pd.read_csv('./treated_data/train_congestion820.csv')
df8 = pd.read_csv('finaldata820.csv')
VI_days3 = df7.loc[df7.loc[:, 'VI_days_before_last_booking'] > 0]
dates= []
for i in VI_days3['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)):
    time = (df8.loc[(df8['date'] == dates[i])]['dep_soll'])
    if len(time) > 0:
        print("hello")
        for j in range(len(time)):
            Vi = df7.loc[df7['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df7.loc[df7['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:

                print("VI : ", Vi, " Cap", cap)
                y.append(0)
            dates_1.append(dates[i])
            times.append(time.iloc[j])


#data set 5
df9= pd.read_csv('./treated_data/train_congestion818.csv')
df10 = pd.read_csv('finaldata818.csv')
VI_days3 = df9.loc[df9.loc[:, 'VI_days_before_last_booking'] > 0]
dates= []
for i in VI_days3['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)):
    time = (df10.loc[(df10['date'] == dates[i])]['dep_soll'])
    if len(time) > 0:

        for j in range(len(time)):
            Vi = df9.loc[df9['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df9.loc[df9['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:

                print("VI : ", Vi, " Cap", cap)
                y.append(0)
            dates_1.append(dates[i])
            times.append(time.iloc[j])

#data set 6
df11= pd.read_csv('./treated_data/train_congestion835.csv')
df12 = pd.read_csv('finaldata835.csv')
VI_days3 = df11.loc[df11.loc[:, 'VI_days_before_last_booking'] > 0]
dates= []
for i in VI_days3['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)):
    time = (df12.loc[(df12['date'] == dates[i])]['dep_soll'])
    if len(time) > 0:

        for j in range(len(time)):
            Vi = df11.loc[df11['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df11.loc[df11['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:

                print("VI : ", Vi, " Cap", cap)
                y.append(0)
            dates_1.append(dates[i])
            times.append(time.iloc[j])


#data set 7

#data set 6
df13 = pd.read_csv('./treated_data/train_congestion834.csv')
df14 = pd.read_csv('finaldata834.csv')
VI_days3 = df13.loc[df13.loc[:, 'VI_days_before_last_booking'] > 0]
dates= []
for i in VI_days3['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)):
    time = (df14.loc[(df14['date'] == dates[i])]['dep_soll'])
    if len(time) > 0:
        print("hello")
        for j in range(len(time)):
            Vi = df13.loc[df13['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df13.loc[df13['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:

                print("VI : ", Vi, " Cap", cap)
                y.append(0)
            dates_1.append(dates[i])
            times.append(time.iloc[j])

#data set 8
df15 = pd.read_csv('./treated_data/train_congestion833.csv')
df16 = pd.read_csv('finaldata833.csv')
VI_days3 = df15.loc[df15.loc[:, 'VI_days_before_last_booking'] > 0]
dates= []
for i in VI_days3['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)):
    time = (df16.loc[(df16['date'] == dates[i])]['dep_soll'])
    if len(time) > 0:
        print("hello")
        for j in range(len(time)):
            Vi = df15.loc[df15['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df15.loc[df15['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:

                print("VI : ", Vi, " Cap", cap)
                y.append(0)
            dates_1.append(dates[i])
            times.append(time.iloc[j])

# data set 9
df17 = pd.read_csv('./treated_data/train_congestion5.csv')
df18 = pd.read_csv('finaldata5.csv')
VI_days3 = df17.loc[df17.loc[:, 'VI_days_before_last_booking'] > 0]
dates= []
for i in VI_days3['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)):
    time = (df18.loc[(df18['date'] == dates[i])]['dep_soll'])
    if len(time) > 0:

        for j in range(len(time)):
            Vi = df17.loc[df17['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df17.loc[df17['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:
                print("VI : ", Vi, " Cap", cap)
                y.append(0)
            dates_1.append(dates[i])
            times.append(time.iloc[j])
# data set 10
df19 = pd.read_csv('./treated_data/train_congestion1.csv')
print(df19.loc[df19['VI']>5])
df20 = pd.read_csv('finaldata.csv')
VI_days3 = df19.loc[df19.loc[:, 'VI_days_before_last_booking'] > 0]
dates= []
for i in VI_days3['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)):
    time = df20.loc[(df20['date'] == dates[i])]['dep_soll']
    if len(time) > 0:
        print("hello")
        for j in range(len(time)):
            Vi = df19.loc[df19['Unnamed: 0'] == dates[i]]['VI'].values
            cap = df19.loc[df19['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:

                print("VI : ", Vi, " Cap", cap)
                y.append(0)
            dates_1.append(dates[i])
            times.append(time.iloc[j])
# data set 11
df21 = pd.read_csv('./treated_data/train_congestion4.csv')
df22 = pd.read_csv('finaldata5.csv')
print(df21.loc[df21['VI']>10])
VI_days3 = df21.loc[df21.loc[:, 'VI_days_before_last_booking'] > 0]
print(VI_days3)
dates= []
for i in VI_days3['Unnamed: 0']:
    dates.append(i)

for i in range(len(dates)):
    time = df22.loc[(df22['date'] == dates[i])]['dep_soll']

    if len(time) > 0:
        for j in range(len(time)):
            Vi = df21.loc[df21['Unnamed: 0'] == dates[i]]['VI'].values
            print(Vi)
            cap = df21.loc[df21['Unnamed: 0'] == dates[i]]['capacity'].values
            if Vi >= cap:
                y.append(1)
            else:

                print("VI : ", Vi, " Cap", cap)
                y.append(0)
            dates_1.append(dates[i])
            times.append(time.iloc[j])

list = list(zip(dates_1, times,y))
weather = pd.read_excel('weather_for_brig.xlsx')
weather[['validdate','time']] = weather['validdate'].str.split('T',expand=True)

matrixdf = pd.DataFrame(list, columns=['date', 'time', 'y'])
print(len(y))


weather = weather.set_index('validdate')
result = matrixdf.join(weather, on ='date', how='inner',lsuffix='_left', rsuffix='_right')

result.drop('snow_depth:cm', inplace = True, axis =1)

result.drop('time_right', inplace = True, axis =1)

result.drop('weather_symbol_1h:idx', inplace = True, axis =1)
result.drop('effective_cloud_cover:octas', inplace = True, axis =1)
result.drop('station_id', inplace = True, axis =1)
result.drop('Unnamed: 0', inplace = True, axis =1)

result[['int_time', 'mins', 'seconds']] = result['time_left'].str.split(':', expand = True)
result[['year', 'month', 'day']] = result['date'].str.split('-', expand = True)
result['month'] = result['month'].astype(int)
result['int_time'] = result['int_time'].astype(int)
from scipy.stats import pearsonr
import seaborn as sns

categories = ['y', 't_2m:C', 'precip_24h:mm']
index_cat = [ 'y', 'temperature', 'precipitation']
heatmap_dict = {}
values = []
for i in range(0, len(categories)):
    for j in range (0, len(categories)):
        corr, _ = pearsonr(result[categories[j]],result[categories[i]])

        if corr < 0:
             corr = corr * (-1)
        values.append(corr)
    heatmap_dict[index_cat[i]] = values
    values = []

print(heatmap_dict)
heatmap_matrix_df = pd.DataFrame(heatmap_dict, index=index_cat)
print(heatmap_matrix_df)
graph = sns.heatmap(heatmap_matrix_df, cmap='Blues')
#figure = graph.get_figure()
#figure.savefig('heatmap2.png', dpi = 400)
onlinelinearregre = result
#onlinelinearregre.drop('time_left', inplace = True, axis =1)
onlinelinearregre.drop('leisure_biking:idx', inplace= True, axis=1)
onlinelinearregre.drop('time_left', inplace=True, axis=1)
onlinelinearregre.drop('date', inplace=True, axis=1)
onlinelinearregre.drop('mins', inplace=True, axis=1)
onlinelinearregre.drop('seconds', inplace=True, axis = 1)
onlinelinearregre.drop('year', inplace=True, axis=1)
onlinelinearregre.drop('month', inplace=True, axis=1)
onlinelinearregre.drop('day', inplace=True, axis=1)
print(onlinelinearregre)
onlinelinearregre.to_excel('online.xlsx')
#result.to_excel('matrix.xlsx')
