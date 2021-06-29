w, h, b = input().split()
print(format(int(w)*int(h)*int(b)/8/1024/1024,'.2f'),'MB',end=' ')