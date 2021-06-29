#for문 사용
a, d, n = map(int, input().split())
for i in range(0,n-1):
    a = a + d
print(a)

#while문 사용
a, d, n = map(int, input().split())
count = 0
while True:
    a = a+d
    count += 1
    if count == n-1:
        print(a)
        break