import pandas as pd

file_path = r'C:\Users\saraf\Desktop\Pinak Idea\Filing-season-statistics-2009-to-current-year.xlsx'
excel_data = pd.ExcelFile(file_path)

sheet_names = excel_data.sheet_names
print(sheet_names)

df = pd.read_excel(file_path, sheet_name='filing-season-statistics-2009-t', skiprows=2)

print(df.columns)

print(df.head())

year_column = 'Year'
num_returns_column = 'Total returnsreceived'

data_2023 = df[df[year_column] == 2023]

num_returns_2023 = data_2023['Total returns\nreceived'].sum()
print(f'Number of tax returns received by IRS in 2023: {num_returns_2023}')
