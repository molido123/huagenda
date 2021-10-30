n=int(input())
for i in range(2,n):
    if n%i==0:
        print("false")
        break
    else:
        if(i==n-1):
            print("true")




