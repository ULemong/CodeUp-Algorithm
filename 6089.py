#for문 사용
a, r, n = map(int, input().split())
for i in range(0,n-1):
    a = a * r
print(a)

#while문 사용
a, r, n = map(int, input().split())
count = 0
while True:
    a = a*r
    count += 1
    if count == n-1:
        print(a)
        break