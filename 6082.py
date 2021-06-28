n = int(input())
for i in range(1, n+1):
    a = i%10
    if (a%3 == 0) and (a != 0):
        i = 'X'
    print(i, end=' ')