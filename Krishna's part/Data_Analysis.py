import numpy as np
import pandas as pd
corr_types = ['int64', 'datetime', 'float64', 'datetime']
df = pd.read_csv(r'C:\Users\41795\Downloads\reservation_data_2019-2021\reservation_data_2019-2021.csv', delimiter=',', low_memory=False)
pd.set_option('display.max_columns', None)
df.drop('abt_char', inplace =True, axis =1)
df.drop('verweis', inplace=True, axis = 1)
df.drop('gr_kkat', inplace = True, axis = 1)
df.drop('tarif', inplace = True, axis =1)
df.drop('pruefzahl', inplace=True, axis=1)
df.drop('ann_tag', inplace=True, axis=1)
df.drop('term_buch', inplace=True, axis=1)
df.drop('term_ann', inplace=True, axis=1)
df.drop('dl', inplace=True, axis=1)
df = df.where(pd.notnull(df), None)
df = df.mask(df.eq('None')).dropna()
#df['res_dt'] = df['res_dt'].astype('datetime')
print(df)

