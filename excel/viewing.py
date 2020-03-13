import pandas as pd
from openpyxl.workbook import Workbook


df = pd.read_csv('names.csv', header=None, delimiter='\t')
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code']
print(df.columns)

# to see based on one column we use
print(df['Last'])
