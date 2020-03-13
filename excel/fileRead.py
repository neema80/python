import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('regions.xlsx') 
df_text = pd.read_csv('data.txt', delimiter='\t')
df_csv = pd.read_csv('names.csv', header=None, delimiter='\t')
# print(df_excel)
# print(df_text)

df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code']
print(df_csv)

# to be able to save changes back to excel we use
# df_csv.to_excel('modified.xlsx')