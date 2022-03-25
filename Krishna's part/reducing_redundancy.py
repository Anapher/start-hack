import pandas as pd

df = pd.read_csv('matrix_1.csv')

pd.set_option('display.max_columns', None)

df[['hours', 'mins', 'seconds']] = df['time_left'].str.split(':', expand = True)

df.drop('mins', inplace = True, axis =1)
df.drop('time_left', inplace = True, axis =1)

df.drop_duplicates(subset='date', keep="first", inplace=True)
df.drop('date', inplace = True, axis =1)
df.drop('seconds', inplace = True, axis =1)
print(df)
df.to_excel('finalmatrix.xlsx')