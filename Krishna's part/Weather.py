import pandas as pd
import numpy as np

df = pd.read_excel('weather.xlsx')
df2 = pd.read_csv('bahnhof.csv')
pd.set_option('display.max_columns', None)
df[['test','station_id']] = df['station_id'].str.split('_',expand=True)
try:
    df2['StationID'] = df2['StationID'].astype(int)
except:
    pass

df.drop('test', inplace = True, axis =1)
#df.to_excel('weather_no_didok.xlsx')
unique_station_id= []
for row in df['station_id']:
    unique_station_id.append(row)
unique_station_id = set(unique_station_id)
unique_station_id = list(unique_station_id)
float_list = [float(i) for i in unique_station_id]
print(unique_station_id)

#print(df2.loc[df2['StationID'] == 87899802])
#for i in float_list :
#    try :
 #      print(df2.loc[df2['StationID'] == i])
  #  except:
   #     print()

#print(df.loc[(df['station_id'] == 8501609)])
df3 = df.loc[df['station_id'] == '8501609']
df3.to_excel('weather_for_brig.xlsx')