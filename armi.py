# arm-interval
a,b=list(map(int,input().split()))
for i in range(a,b+1):
    temp=i
    rev=0
    while i>0:
        rem=i%10
        rev=rev+rem**3
        i=i//10
    if temp==rev:
        print(rev)
