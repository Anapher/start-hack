import numpy as np
import pandas as pd

df = pd.read_csv('./cleaner_data.csv')
pd.set_option('display.max_columns', None)
df = df.loc[(df['line'] == 'IC 8') & (df['train_nr'] == 807)]
df.to_csv('finaldata.csv')