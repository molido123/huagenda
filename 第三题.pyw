now=int(input())
result=(now%4==0 and now%100!=0)or(now%400==0)
print(result)
