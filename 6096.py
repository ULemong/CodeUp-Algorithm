a,b = [],[]

for i in range(19):
    a = list(map(int, input().split()))
    b.append(a)
    a = []

n = int(input())
for i in range(n):
    x, y = input().split()
    for j in range(19):
        if b[int(x)-1][j] == 0:
            b[int(x)-1][j] = 1
        else:
            b[int(x)-1][j] = 0
    for j in range(19):
        if b[j][int(y)-1] == 0:
            b[j][int(y)-1] = 1
        else:
            b[j][int(y)-1] = 0

for i in range(19):
    for j in range(19):
        print(b[i][j], end=' ')
    print()