n = int(input())
sum, i = 0, 0
while sum < n:
    i += 1
    sum += i
    if sum >= n:
        print(sum)

#break 사용
n = int(input())
sum, i = 0, 0
while True:
    i += 1
    sum += i
    if sum >= n:
        break
print(sum)