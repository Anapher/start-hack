import numpy as np
import pandas as pd

df = pd.read_csv('./cleaner_data.csv')
pd.set_option('display.max_columns', None)
df = df.loc[(df['line'] == 'IC 51') & (df['train_nr'] == 1610)]
print(df)
df.to_csv('finaldata3.csv')