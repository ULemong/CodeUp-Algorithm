n = int(input())
a = input().split()
d = []
for i in range(24):
    d.append(0)
for j in range(n):
    d[int(a[j])] += 1
for k in range(1,24):
    print(d[k], end=' ')