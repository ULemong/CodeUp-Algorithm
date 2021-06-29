#for문 사용
a, m, d, n = map(int, input().split())
for i in range(0,n-1):
    a = a*m+d
print(a)

#while문 사용 -> 시간 초과
a, m, d, n = map(int, input().split())
count = 0
while True:
    a = a*m+d
    count += 1
    if count == n-1:
        print(a)
        break