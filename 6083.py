n1, n2, n3 = input().split()
count = 0
for i in range(int(n1)):
    for j in range(int(n2)):
        for k in range(int(n3)):
            print(i,j,k,sep=' ')
            count += 1
print(count)