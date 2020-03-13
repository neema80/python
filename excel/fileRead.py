import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('regions.xlsx') 
# df_text = pd.read_csv('data.txt')
print(df_excel)