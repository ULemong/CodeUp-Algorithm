n = input()
x = int(n, 16)
for i in range(1,16):
    print('%X*%X=%X' % (x,i,x*i))