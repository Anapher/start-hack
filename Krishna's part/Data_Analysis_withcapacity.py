import numpy as np
import pandas as pd
df = pd.read_csv(r'C:\Users\41795\Downloads\reservation_data_2019-2021_incl_capacity\reservation_data_2019-2021_incl_capacity.csv', delimiter=',', low_memory=False)
pd.set_option('display.max_columns', None)
df.drop('res_delta_ist', inplace = True, axis =1)
df.drop('res_delta_soll', inplace = True, axis =1)
df.drop('res_delta_valid', inplace = True, axis =1)

df[['res_dt','test']] = df['res_dt'].str.split(' ',expand=True)
df[['date','test']] = df['date'].str.split(' ',expand=True)
df[['test','dep_ist']] = df['dep_ist'].str.split(' ',expand=True)
df[['test','dep_soll']] = df['dep_soll'].str.split(' ',expand=True)



df.drop('test', inplace = True, axis =1)


train_nr = []
for row in df['train_nr']:
    train_nr.append(row)

unique_trains = set(train_nr)
unique_trains= list(unique_trains)
best_values = {}
def mostoccurent(values) :
    counter = 0
    num = values[0]
    set_value = set(values)
    set_value = list(set_value)
    length = len(set_value)
    for i in set_value:
        curr_frequency = values.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num

for train in unique_trains:
    for capacity in df.loc[df['train_nr'] == train]['capacity']:
        values = []
        if capacity > 0 :
            values.append(capacity)
    if len(values) > 0 :
        highestoccurent = mostoccurent(values)
        best_values[train] = highestoccurent
    else :
        print(train)

#df = df.replace({np.nan: None})
df = df.fillna(value = -1)
print(df.loc[(df['train_nr'] == 333) & (df['capacity'] == -1)])

for train in unique_trains:
    print(best_values.get(train))
    try :
        index = df.index[(df['train_nr'] == train) & (df['capacity'] == -1)]
        for i in index :
            df.at[i, 'capacity'] = best_values.get(train)


    except:
        pass

print(df)
#df.to_csv("cleaner_data.csv")
