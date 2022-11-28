import itertools
import random

N = 100
numArray = []
counts = []

for i in range(N):
    numArray.append(random.randint(0, 1))


def show_subsequence(count):
    if count > 0:
        return "".join(itertools.repeat("0", count))
    else:
        return "".join(itertools.repeat("1", count * -1))


tempValue = numArray[0]
tempCount = 1

print(numArray)

# отрицательное значение = 1, положительное = 0
for item in numArray[1:]:
    if tempValue == item:
        tempCount += 1
    else:
        if tempValue == 0:
            counts.append(tempCount)
            tempValue = 1
        else:
            counts.append(tempCount * -1)
            tempValue = 0
        tempCount = 1

if tempValue == 0:
    counts.append(tempCount)
else:
    counts.append(tempCount * -1)

for k in set(counts):
    print(f"{show_subsequence(k)}: {(counts.count(k) / len(counts)) * 100}%")



