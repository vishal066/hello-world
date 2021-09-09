n=int(input("enter the length of the series"))
i=0
a=0
b=1
print(a)
print(b)

while i<=n-3:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
