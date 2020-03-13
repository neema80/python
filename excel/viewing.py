import pandas as pd
from openpyxl.workbook import Workbook


df = pd.read_csv('names.csv', header=None, delimiter='\t')
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code']
print(df.columns)

# to see based on one column we use
print(df['Last'])

# for multiple comulumns should enter double brackets
print(df[['Last','State']])

# if the list is too long can use slicing as below
print(df['Last'][0:3])

# to be able to see based on row location
print(df.iloc[1])

# even to get to cell should use the following style
# iloc[row starting from 0 , columns starting from 0] i.e
print(df.iloc[2,1])

# if want to extract some part and to save them separately shold use the following
wanted_values = df[['First', 'Last', 'Area Code']]
stored = wanted_values.to_excel('State Location.xlsx', index=None)
