# Importing libraries
import pandas as pd

# Read csv file into a pandas dataframe
excel_file_input_path = 'Populations.csv'
columns=[]
for i in range (0,58):
    columns.append(i+4)
df = pd.read_csv(excel_file_input_path, skiprows = [0, 1, 2, 3], usecols=columns[0:58])

df.columns = df.columns.str.replace('-', '')
print(df)
#df["1960"].replace({"19112112=11": "191121"}, inplace=True)
#
# for i in range(0,62):
#     print(df.iat[0, i])
#     if (df.iat[0, i] == 'ERR') :
#         df.iat[0, i] = (pd.to_numeric(df.iat[0, i-1]) + pd.to_numeric(df.iat[0, i+1])) / 2
#
# for i in range(1,62):
#     print(df.iat[1, i])
#     if (df.iat[1, i] == 'ERR') :
#         df.iat[1, i] = (pd.to_numeric(df.iat[1, i-1]) + pd.to_numeric(df.iat[1, i+1])) / 2
#
df2 = pd.read_csv(excel_file_input_path, usecols={0,1,2,3}, skiprows=[0,1,2,3])
print(df2)
df.replace(r'\d*\D{1,4}\d*','', regex=True, inplace= True,)
for i in range(0, 264):
    for j in range (0, 57):
        if (df.iat[i, j] == ''):
            df.iat[i, j] = ((pd.to_numeric(df.iat[i, j - 1]) + pd.to_numeric(df.iat[i, j + 1])) / 2)
df_row = pd.concat([df2, df], axis=1)




print(df_row)
# Print to the output file
excel_file_output_path = "CleanPopulation.csv"
# df.to_csv(excel_file_output_path)
df_row.to_csv(excel_file_output_path)
