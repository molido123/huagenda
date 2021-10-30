a=input("").split()
b=int(a[0])+int(a[1])+int(a[2])
print(b," ",end="")
r=int(a[0])
p=int(a[1])
q=int(a[2])
s2=(b/2)*(b/2-r)*(b/2-p)*(b/2-q)
s=s2**0.5
print(s," ",end="")
if r**2+p**2==q**2:
    print("True")
elif r**2+q**2==p**2:
    print("True")
elif p**2+q**2==r**2:
    print("True")
else:
    print("False")