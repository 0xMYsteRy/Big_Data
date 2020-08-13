# Importing libraries
import pandas as pd

# Read csv file into a pandas dataframe
excel_file_input_path = 'Populations.csv'

# Split the excel file into 2 files then merge together.
columns = []
for i in range(0, 58):
    columns.append(i + 4)

df = pd.read_csv(excel_file_input_path, skiprows=[0, 1, 2, 3], usecols=columns[0:58])

# Replace all the column contains '-' character.(E.g: 19-99 to 1999)
df.columns = df.columns.str.replace('-', '')

# Split the excel file into 2 files then merge together.
df2 = pd.read_csv(excel_file_input_path, usecols={0, 1, 2, 3}, skiprows=[0, 1, 2, 3])

# Replace all '=' characters
df.replace(r'\d*\D{1,4}\d*', '', regex=True, inplace=True, )

# Convert datatype, check the datatype with the following command: df.info()
itemlist = ['1984', '1985', '1993', '2007', '2008', '2009']
for item in itemlist:
    df[item] = df[item].astype('object')

# Handling missing value:
for i in range(0, 264):
    for j in range(0, 57):
        # Flip the negative value into positive one.
        if pd.to_numeric(df.iat[i, j]) < 0:
            df.iat[i, j] = pd.to_numeric(df.iat[i, j] * (-1))

        # Handling missing value between two known adjacent values.
        if pd.isnull(df.iat[i, j]):
            df.iat[i, j] = ((pd.to_numeric(df.iat[i, j - 1]) + pd.to_numeric(df.iat[i, j + 1])) / 2)
        # Handling missing value in the year 1960 (Outer left column)
        if df.iat[i, 0] == '' or pd.to_numeric(df.iat[i, 0]) == 0:
            df.iat[i, 0] = df.iat[i, 1]
        # Handling missing value in the year 2017 (Outer right column)
        if df.iat[i, 57] == '':
            print("Acces this loop")
            df.iat[i, 57] = df.iat[i, 56]
        if df.iat[i, j] == '':
            df.iat[i, j] = ((pd.to_numeric(df.iat[i, j - 1]) + pd.to_numeric(df.iat[i, j + 1])) / 2)
            if df.iat[i, j + 1] == '':
                df.iat[i, j] = df.iat[i, j - 1]
                df.iat[i, j + 1] = df.iat[i, j + 2]
# Append the file in the horizontal direction
df_row = pd.concat([df2, df], axis=1)

# Convert the column type from float64 to object
itemlist = ['1984', '1985', '1993', '2007', '2008', '2009']
for item in itemlist:
    df_row[item] = df_row[item].astype('object')

# Write data to the output file
excel_file_output_path = "CleanPopulation.csv"
df_row.to_csv(excel_file_output_path)
