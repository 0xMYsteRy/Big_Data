# RMIT University Vietnam
# Course: EEET2574 Big Data in Engineering
# Semester: 2020B
# Assessment: Statistical Analysis
# Author: Nguyen Le
# Created date: 10/08/2020
# Last modified date: 16/08/2020
# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read csv file into a pandas dataframe
excel_file_input_path = 'Populations.csv'

# Split the excel file into 2 files then merge together.
columns = []
for i in range(0, 58):
    columns.append(i + 4)
df = pd.read_csv(excel_file_input_path, skiprows=[0, 1, 2, 3], usecols=columns[0:58])

# Replace all the column contains '-' character (E.g: 19-99 to 1999), handling illegal datatype.
df.columns = df.columns.str.replace('-', '')

# Split the excel file into 2 files then merge together.
df2 = pd.read_csv(excel_file_input_path, usecols={0, 1, 2, 3}, skiprows=[0, 1, 2, 3])

# Replace all '=' characters
df.replace(r'\d*\D{1,4}\d*', '', regex=True, inplace=True, )

# Convert datatype, check the datatype with the following command: df.info()
#df.info()
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

# Remove the rows

df_row.drop([90, 108, 194, 212, 223], inplace= True)
# print(df_row.head())

# Write data to the output file
excel_file_output_path = "CleanPopulation.csv"
df_row.to_csv(excel_file_output_path)

# ----------*****----------
# Plotting
df_plot = df_row.copy()

# Find the first digit
def firstDigit(num):
    n = num
    while n >= 10:
        n = n // 10
    return n

# Create an array first digit int in the year 2010, column = 54
num_list = []
i = 0

while (i <= 258):
    a = pd.to_numeric(df_plot.iat[i, 54])
    num_list.append(a)
    i = i+1
print(num_list)

# Create a list of first int and count their occurences.
num = 0
firstDigitDict = {}
while num < 258:
    key = firstDigit(num_list[num])
    if key not in firstDigitDict:
        firstDigitDict[key] = 1
    else:
        firstDigitDict[key] += 1
    num += 1
print("The first digits in the year 2010 are: ")
print(firstDigitDict)

# Percent of firstDigit of the year 2010
first_numbers_percent = {}
for key, num in firstDigitDict.items():
    first_numbers_percent[key] = 100.0 * num / 258.0

print("First digit percentile: ")
print(first_numbers_percent)

# First digit plotting for bar chart
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y_values = [26.7, 16.7, 14.3, 8.5, 10.8, 6.6, 5.0, 7.0, 4.2]
plt.title("Country Population First Digit Distribution in 2010")
plt.xlabel("First Digit Number")
plt.xticks([1,2,3,4,5,6,7,8,9])
plt.ylabel("Percentile")
plt.bar(x_values, y_values, color='royalblue')
plt.scatter(x_values, y_values, s=10, c='burlywood')  # dot
plt.figure(dpi=256, figsize=(50, 30))
plt.show()

# First digit plotting for line chart
plt.title("Country Population First Digit Distribution in 2010")
plt.xlabel("First Digit Number")
plt.xticks([1,2,3,4,5,6,7,8,9])
plt.ylabel("Percentile")
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [26.7, 16.7, 14.3, 8.5, 10.8, 6.6, 5.0, 7.0, 4.2], s=20, c='blue')  # dot
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [26.7, 16.7, 14.3, 8.5, 10.8, 6.6, 5.0, 7.0, 4.2])
plt.show()

# Find the last digit
def lastDigit(num):
    n = num
    return n % 10

# Count the last digit
num2 = 0
lastDigitDict = {}
while num2 < 258:
    key2 = lastDigit(num_list[num2])
    if key2 not in lastDigitDict:
        lastDigitDict[key2] = 1
    else:
        lastDigitDict[key2] += 1
    num2 += 1
print("The last digits are:")
print(lastDigitDict)

# percent of lastDigit
last_numbers_percent = {}
for key2, num2 in lastDigitDict.items():
    last_numbers_percent[key2] = 100 * num2 / 258
print("Last digit percentile: ")
print(last_numbers_percent)

# Last digit plotting for bar chart
x_values2 = [0,1,2,3,4,5,6,7,8,9]
y_values2 = [18.6, 11.2, 9.7, 9.7, 10.0, 9.7, 8.1, 7.8, 4.6, 8.5]
plt.title("Country Population Last Digit Distribution in 2010")
plt.xlabel("Last Digit Number")
plt.xticks([1,2,3,4,5,6,7,8,9])
plt.ylabel("Percentile")
plt.bar(x_values2, y_values2, color='blue')
plt.scatter(x_values2, y_values2, s=10, c='blue')  # dot
plt.figure(dpi=128, figsize=(10, 6))
plt.show()

# Last digit plotting for line chart
plt.title("Country Population Last Digit Distribution in 2010")
plt.xlabel("Last Digit Number")
plt.xticks([1,2,3,4,5,6,7,8,9])
plt.ylabel("Percentile")
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [18.6, 11.2, 9.7, 9.7, 10.0, 9.7, 8.1, 7.8, 4.6, 8.5], s=20, c='blue')  # dot
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [18.6, 11.2, 9.7, 9.7, 10.0, 9.7, 8.1, 7.8, 4.6, 8.5])
plt.show()

# First digit plotting from 1980 - 2017
plt.title("Country Population First Digit Distribution 1980 - 2017")
plt.xlabel("First Digit Number")
plt.xticks([1,2,3,4,5,6,7,8,9])
plt.ylabel("Percentile")
#In 1980: {6: 6.6, 1: 27.9, 8: 4.7, 2: 14.7, 3: 18.2, 7: 5.8, 4: 8.5, 9: 6.2, 5: 7.4}
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.9, 16.7, 18.2, 8.5, 7.4, 6.6, 5.8, 4.7, 6.2], s=20, c='blue', label='1980')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.9, 16.7, 18.2, 8.5, 7.4, 6.6, 5.8, 4.7, 6.2])

#In 1985: {6: 7.0, 1: 31.0, 2: 13.2, 4: 11.6, 3: 16.7, 7: 6.2, 9: 4.7, 8: 3.5, 5: 6.2}
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [31.0, 13.2, 16.7, 11.6, 6.2, 7.0, 6.2, 3.5, 4.7], s=20, c='green', label='1985')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [31.0, 13.2, 16.7, 11.6, 6.2, 7.0, 6.2, 3.5, 4.7], c='green')

#In 1990: {6: 4.3, 1: 27.9, 3: 12.8, 5: 10.5, 2: 15.9, 4: 13.6, 7: 5.4, 9: 4.6, 8: 5.0}
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.9, 15.9, 12.8, 13.6, 10.5, 4.3, 5.4, 5.0, 4.6], s=20, c='purple', label='1990')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.9, 15.9, 12.8, 13.6, 10.5, 4.3, 5.4, 5.0, 4.6], c='purple')

#In 1995: {8: 3.1, 1: 27.5, 3: 12.0, 6: 3.5, 2: 17.1, 5: 12.4, 7: 6.6, 4: 12.8, 9: 5.0}
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.5, 17.1, 12.0, 12.8, 12.4, 3.5, 6.6, 3.1, 5.0], s=20, c='orange', label='1995')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.5, 17.1, 12.0, 12.8, 12.4, 3.5, 6.6, 3.1, 5.0], c='orange')

#In 2000: {9: 3.1, 2: 16.7, 1: 27.5, 3: 13.2, 6: 10.1, 5: 8.9, 8: 6.6, 7: 2.7, 4: 11.2}
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.5, 16.7, 13.2, 11.2, 8.9, 10.1, 2.7, 6.6, 3.1], s=20, c='red', label='2000')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.5, 16.7, 13.2, 11.2, 8.9, 10.1, 2.7, 6.6, 3.1], c='red')

#In 2005: {1: 27.5, 2: 16.7, 3: 13.6, 7: 7.0, 4: 12.0, 5: 8.5, 8: 5.4, 9: 2.7, 6: 6.6}
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.5, 16.7, 13.2, 11.2, 8.9, 10.1, 2.7, 6.6, 3.1], s=20, c='cyan', label='2005')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [27.5, 16.7, 13.2, 11.2, 8.9, 10.1, 2.7, 6.6, 3.1], c='cyan')

#In 2010: [26.7, 16.7, 14.3, 8.5, 10.8, 6.6, 5.0, 7.0, 4.2]
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [26.7, 16.7, 14.3, 8.5, 10.8, 6.6, 5.0, 7.0, 4.2], s=20, c='magenta', label='2010')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [26.7, 16.7, 14.3, 8.5, 10.8, 6.6, 5.0, 7.0, 4.2], c='magenta')

#In 2015: {1: 29.8, 3: 14.3, 2: 14.3, 7: 6.2, 9: 5.4, 4: 9.3, 5: 10.0, 8: 3.5, 6: 6.6}
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [29.8, 14.3, 14.3, 9.3, 10.0, 6.6, 6.2, 6.2, 5.4], s=20, c='lime', label='2015')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [29.8, 14.3, 14.3, 9.3, 10.0, 6.6, 6.2, 6.2, 5.4], c='lime')

#In 2017: {1: 29.8, 3: 12.8, 2: 15.1, 7: 4.3, 4: 10.9, 9: 5.0, 5: 9.3, 8: 4.6, 6: 7.8}
plt.scatter([1, 2, 3, 4, 5, 6, 7, 8, 9], [29.8, 15.1, 12.8, 10.9, 9.3, 7.8, 4.3, 4.6, 5.0], s=20, c='dodgerblue', label='2017')
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [29.8, 15.1, 12.8, 10.9, 9.3, 7.8, 4.3, 4.6, 5.0], c='dodgerblue')
plt.legend(loc='best')
plt.show()

# Last digit plotting from 1980 - 2017
plt.title("Country Population Last Digit Distribution 1980 - 2017")
plt.xlabel("Last Digit Number")
plt.xticks([0,1,2,3,4,5,6,7,8,9])
plt.ylabel("Percentile")
#In 1980: 6: 9.3, 0: 20.2, 7: 9.7, 4: 7.8, 8: 9.3, 1: 8.9, 2: 9.7, 3: 7.0, 5: 11.6, 9: 6.6}
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [20.2, 8.9, 9.7, 7.0, 7.8, 11.6, 9.3, 7.8, 9.3, 6.6], s=20, c='blue', label='1980')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [20.2, 8.9, 9.7, 7.0, 7.8, 11.6, 9.3, 7.8, 9.3, 6.6])

#In 1985: {6: 12.0, 0: 13.9, 2: 10.5, 1: 9.7, 3: 9.7, 5.0: 9.7, 8.0: 12.4, 7: 8.1, 4: 7.0, 9: 7.0}
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [13.9, 9.7, 10.5, 9.7, 7.0, 9.7, 12.0, 8.1, 12.4, 7.0], s=20, c='green', label='1985')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [13.9, 9.7, 10.5, 9.7, 7.0, 9.7, 12.0, 8.1, 12.4, 7.0], c='green')

#In 1990: {9: 8.5, 4: 10.5, 1: 9.7, 2: 10.0, 6: 10.5, 5: 11.2, 8: 10.1, 0: 17.4, 7: 5.8, 3: 6.2}
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [17.4, 9.7, 10.0, 6.2, 10.5, 11.2, 10.5, 5.8, 10.1, 8.5], s=20, c='purple', label='1990')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [17.4, 9.7, 10.0, 6.2, 10.5, 11.2, 10.5, 5.8, 10.1, 8.5], c='purple')

#In 1995: {4: 10.5, 1: 8.9, 0: 17.1, 2: 9.3, 8: 8.9, 9: 9.7, 7: 9.3, 3: 8.1, 6: 10.5, 5: 7.8}
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [17.1, 8.9, 8.1, 10.5, 7.8, 10.5, 10.5, 9.3, 8.9, 9.7], s=20, c='orange', label='1995')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [17.1, 8.9, 8.1, 10.5, 7.8, 10.5, 10.5, 9.3, 8.9, 9.7], c='orange')

#In 2000: {6: 11.0, 3: 7.4, 7: 9.3, 4: 7.4, 0: 13.9, 1: 8.2, 5: 7.5, 9: 8.9, 8: 8.5, 2: 8.1}
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [13.9, 8.3, 8.1, 7.4, 7.4, 7.5, 11.0, 9.3, 8.5, 8.9], s=20, c='red', label='2000')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [13.9, 8.3, 8.1, 7.4, 7.4, 7.5, 11.0, 9.3, 8.5, 8.9], c='red')

#In 2005: {1: 8.5, 8: 10.0, 2: 8.9, 7: 10.9, 9: 8.1, 3: 7.8, 0: 13.9, 5: 8.9, 4: 11.2, 6: 10.9}
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [13.9, 8.5, 8.9, 7.8, 11.2, 8.9, 10.9, 7.8, 10.0, 8.1], s=20, c='cyan', label='2005')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [13.9, 8.5, 8.9, 7.8, 11.2, 8.9, 10.9, 7.8, 10.0, 8.1], c='cyan')

#In 2010: [18.6, 11.2, 9.7, 9.7, 10.0, 9.7, 8.1, 7.8, 4.6, 8.5]
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [18.6, 11.2, 9.7, 9.7, 10.0, 9.7, 8.1, 7.8, 4.6, 8.5], s=20, c='magenta', label='2010')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [18.6, 11.2, 9.7, 9.7, 10.0, 9.7, 8.1, 7.8, 4.6, 8.5], c='magenta')

#In 2015: {1: 10.1, 4: 9.3, 5: 9.3, 3: 12.8, 0: 11.2, 2: 9.7, 7: 10.5, 9: 12.8, 6: 5.8, 8: 7.8}
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [11.2, 10.1, 9.7, 12.8, 9.3, 9.3, 5.8, 10.5, 7.8, 12.8], s=20, c='lime', label='2015')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [11.2, 10.1, 9.7, 12.8, 9.3, 9.3, 5.8, 10.5, 7.8, 12.8], c='lime')

#In 2017: {4: 9.7, 1: 11.6, 3: 9.7, 7: 9.7, 5: 7.8, 6: 6.6, 0: 15.1, 2: 9.7, 9: 8.5, 8: 11.2}
plt.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [15.1, 11.6, 9.7, 9.7, 9.7, 7.8, 6.6, 9.7, 11.2, 8.5], s=20, c='dodgerblue', label='2017')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [15.1, 11.6, 9.7, 9.7, 9.7, 7.8, 6.6, 9.7, 11.2, 8.5], c='dodgerblue')

plt.legend(loc='upper right')
plt.figure(dpi=128, figsize=(10, 6))
plt.show()

# -----------------------------

# This part is for question 2, please kindly
# download the data set from this URL then uncomment the code.
# URL: https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# from pandas.api.types import is_numeric_dtype
#
# df_iris = pd.read_csv('iris.csv')
# print('Determine the mean value: ')
# print(df_iris.groupby('species').agg(['mean']))
# print('\n')
# print('Determine the median value: ')
# print(df_iris.groupby('species').agg(['median']))
# print('\n')
# print('Determine the variance value: ')
# print(df_iris.groupby('species').var())
# print('\n')
# print('Determine the standard deviation: ')
# print(df_iris.groupby('species').std())
# print('Covariance: \n')
# print(df_iris.cov())
# print('Correlation: \n')
# print(df_iris.corr())
#
# sns.set_style("whitegrid")
# sns.pairplot(df_iris, hue="species", size= 3)
# sns.FacetGrid(df_iris, hue="species", size = 4) \
#    .map(sns.distplot, "petal_length") \
#    .add_legend()
# sns.FacetGrid(df_iris, hue="species", size = 4) \
#    .map(sns.distplot, "petal_width") \
#    .add_legend()
# plt.show()
