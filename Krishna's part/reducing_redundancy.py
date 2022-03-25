import pandas as pd

df = pd.read_csv('matrix_1.csv')

pd.set_option('display.max_columns', None)


df.drop_duplicates(subset='date', keep="first", inplace=True)
df.to_excel('finalmatrix.xlsx')