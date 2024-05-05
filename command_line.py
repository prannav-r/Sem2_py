import sys
for i in range (0,len(sys.argv)-1):
    sys.argv[i]=sys.argv[i+1]
print(sys.argv)