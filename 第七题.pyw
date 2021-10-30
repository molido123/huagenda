m=input().split('.')
year=int(m[0])
month=int(m[1])
day=int(m[2])
leap=[0,31,29,31,30,31,30,31,31,30,31,30,31]
norm=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if year<2000:
    print("欧尼酱，不要乱调戏人家")
elif year==2000:
    this=day
    for i in range(1,month):
        this+=leap[i]
    print(this)
elif year>2000:
    sum=0
    for i in range(2000,year):
        if (i%4==0 and i%100!=0)or(i%400==0):
            sum+=366
        else:
            sum+=365
    if (year%4==0 and year%100!=0)or(year%400==0):
           for i in range(1,month):
               sum+=leap[i]
               print(sum)
    else:
        for i in range(1,month):
               sum+=norm[i]
               print(sum)

            



          


