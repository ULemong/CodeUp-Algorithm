n1, n2, n3 = input().split()
a = int(n1)
b = int(n2)
c = int(n3)
print((a if(a<b) else b) if ((a if(a<b) else b)<c) else c)