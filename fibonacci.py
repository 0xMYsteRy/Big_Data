list = [1, 1]

i = 2
line = 0
while (i <= 250):
    a = list[i - 2] + list[i - 1]
    list.append(a)
    i = i + 1
    line += 1
print(list)
# print(line)

# find the first digit
def firstDigit(num):
    n = num
    while (n > 10):
        n = n // 10
    return n

# count the first digit
num = 0
firstDigitDict = {}

while (num < 250):
    key = firstDigit(list[num])
    if key not in firstDigitDict:
        firstDigitDict[key] = 1
    else:
        firstDigitDict[key] += 1
    num += 1

print(firstDigitDict)

# percent of firstDigit
first_numbers_percent = {}
for key,num in firstDigitDict.items():
    first_numbers_percent[key]= num/250


print(first_numbers_percent)

# Plotting
import matplotlib.pyplot as plt
x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [67,43,32,23,21,15,15,14,11,9]
plt.plot(x_values,y_values)
plt.show()