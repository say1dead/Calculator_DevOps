n = int(input())#кол во лаб
arr1 = [] * n
arr2 = [] * n
arr3 = [] * n
r = [0] * n
for i in range(n):
    arr1.insert(i, input())

for i in range(n):
    arr2.insert(i, input())

for i in range(n):
    arr3.insert(i, input())

for i in range(n):
    if arr1[i] == arr2[i]:
        r[0] += 1
        r[1] += 1
print(r)