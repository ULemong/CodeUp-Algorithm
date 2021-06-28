n = int(input())
sum, i = 0, 0
while sum < n:
    i += 1
    sum += i
    if sum >= n:
        print(i)