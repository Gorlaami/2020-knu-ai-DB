import numpy as np

a = np.array([4, 5, 1, 0, 11, 2], int)
print(a)
i = 0
k = 1
number = int(input())
while True:
    k = 0
    for i in range(0, len(a) - 1):
        if a[i] <= a[i + 1]:
            pass
        else:
            a[i], a[i + 1] = a[i + 1], a[i]
            k += 1
    if k == 0:
        break
print(a)
low = 0
high = len(a) - 1
while low <= high:
    mid = (low + high) // 2
    if number < a[mid]:
        high = mid - 1
    elif number > a[mid]:
        low = mid + 1
    else:
        print("ID =", mid)
        break
else:
    print("No the number")


