n = int(input())
a,b = [],[]

for i in range(19):
    for j in range(19):
        a.append(0)
    b.append(a)
    a = []
#b = [[0 for j in range(19)] for i in range(19)] -> 위와 같은 내용

for i in range(n):
    x, y = list(map(int, input().split()))
    b[x - 1][y - 1] = 1

for i in range(19):
    for j in range(19):
        print(b[i][j], end=' ')
    print()