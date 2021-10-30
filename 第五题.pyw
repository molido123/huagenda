s=input().split()
a=int(s[0])
n=int(s[1])
piece=""
sum=0
for i in range(1,n+1):
    p=i
    for i in range(1,p+1):
        piece+=s[0]
    sum+=int(piece)
    piece=""
print(sum)