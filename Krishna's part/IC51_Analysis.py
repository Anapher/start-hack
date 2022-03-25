import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('./finaldata3.csv')
pd.set_option('display.max_columns', None)
unique_locations = []
for row in df['bp_from']:
    unique_locations.append(row)

unique_locations = set(unique_locations)
unique_locations = list(unique_locations)
print(unique_locations)