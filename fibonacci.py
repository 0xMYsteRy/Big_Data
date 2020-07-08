import matplotlib.pyplot as plt
import numpy as np

fibonacci_list = [1, 1]

i = 2
while (i <= 250):
    a = fibonacci_list[i - 2] + fibonacci_list[i - 1]
    fibonacci_list.append(a)
    i = i + 1
print("The first 250 fibonacci numbers: ")
print(fibonacci_list)
print("----------*****----------")


# find the first digit
def firstDigit(num):
    n = num
    while n > 10:
        n = n // 10
    return n


# find the last digit
def lastDigit(num):
    n = num
    return n % 10


# count the first digit
num = 0
firstDigitDict = {}
while num < 250:
    key = firstDigit(fibonacci_list[num])
    if key not in firstDigitDict:
        firstDigitDict[key] = 1
    else:
        firstDigitDict[key] += 1
    num += 1
print("The first digits are: ")
print(firstDigitDict)

# count the last digit
num2 = 0
lastDigitDict = {}
while num2 < 250:
    key2 = lastDigit(fibonacci_list[num2])
    if key2 not in lastDigitDict:
        lastDigitDict[key2] = 1
    else:
        lastDigitDict[key2] += 1
    num2 += 1
print("The last digits are:")
print(lastDigitDict)
print("----------*****----------")

# percent of firstDigit
first_numbers_percent = {}
for key, num in firstDigitDict.items():
    first_numbers_percent[key] = 100 * num / 250

print("First digit percentile: ")
print(first_numbers_percent)

# percent of lastDigit
last_numbers_percent = {}
for key2, num2 in lastDigitDict.items():
    last_numbers_percent[key2] = num2 / 2.5

print("Last digit percentile: ")
print(lastDigitDict)

# First digit plotting
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [26.8, 17.2, 12.8, 9.2, 8.4, 6.0, 6.0, 5.6, 4.4, 3.6]
plt.title("Fibonacci First Digit Distribution (Sample n = 250)")
plt.xlabel("Numbers")
plt.ylabel("Percentile")
plt.bar(x_values, y_values, color='royalblue')
plt.scatter(x_values, y_values, s=10, c='burlywood')  # dot
plt.figure(dpi=256, figsize=(50, 30))
plt.show()

# Last digit plotting
x_values2 = []
y_values2 = []

x_values2 = list(lastDigitDict.keys())
y_values2 = list(last_numbers_percent.values())
plt.title("Fibonacci Last Digit Distribution (Sample n = 250)")
plt.xlabel("Numbers")
plt.ylabel("Percentile")
plt.bar(x_values2, y_values2, color='crimson')
plt.scatter(x_values2, y_values2, s=10, c='burlywood')  # dot
plt.figure(dpi=256, figsize=(50, 30))

plt.show()


