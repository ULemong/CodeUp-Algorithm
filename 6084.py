h, b, c, s = input().split()
print(format(int(h)*int(b)*int(c)*int(s)/8/1024/1024,".1f"),'MB',end=' ')