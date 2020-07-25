import matplotlib.pyplot as plt
import random
Num = 1000
mod = [0] * 10
for i in range(Num):
    mod[random.randint(0, 9)] += 1

x_values = list(range(10))
for i in range(0, 10):
    mod[i] = mod[i] / float(Num)

plt.title("Random Numbers", fontsize=24)
plt.xlabel("Integers", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
plt.axis([0, 9, 0, 1])
plt.scatter(x_values, mod, s=10)
plt.show()

