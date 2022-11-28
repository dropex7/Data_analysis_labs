import numpy as np
from matplotlib import pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
y = np.array([10, 13, 22, 24, 33, 36, 40, 60, 93, 49, 59, 76, 81, 100, 120, 22, 150, 100, 140, 80])

print(f"Математическое ожидание: {np.mean(y)}")
print(f"Среднеквадратичное отклонение: {np.std(y)}")

t = np.polyfit(x, y, 4)
f = np.poly1d(t)

plt.scatter(x, y)
plt.plot(x, f(x), 'g')
plt.show()
