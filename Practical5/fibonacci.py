a=1 #a1
b=1 #a2
print(a)
print(b)
c=0
for i in range (0,11):#a3 to a13
    c=a+b #a(n+1) = a(n-1) + a(n)
    a=b #change a(n-1) to a(n)
    b=c #change a(n) to a(n+1)
    print(c)
