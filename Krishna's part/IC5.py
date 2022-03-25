import numpy as np
import pandas as pd

df = pd.read_csv('./cleaner_data.csv')
pd.set_option('display.max_columns', None)
df = df.loc[(df['line'] == 'IC 5')& (df['train_nr'] == 525)]
print(df)
df.to_csv('finaldata4.csv')