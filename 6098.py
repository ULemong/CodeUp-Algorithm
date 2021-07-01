a,b = [],[]
j = 1
breaker = False

for i in range(10):
    a = list(map(int, input().split()))
    b.append(a)
    a = []

for i in range(1,9):
    for j in range(j,9):
        if b[i][j] == 2:
            b[i][j] = 9
            breaker = True
            break
        if b[i][j+1] == 1:
            b[i][j] = 9
            break
        else:
            b[i][j] = 9
    if breaker == True:
        break

for i in range(10):
    for j in range(10):
        print(b[i][j], end=' ')
    print()