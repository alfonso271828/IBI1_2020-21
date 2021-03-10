a=1
b=1
print(a)
print(b)
for i in range (1,6):
    a= a+b # the (2*i+1)th number 
    b=a+b # the (2*i+2)th number
    print (a)
    print (b)
a= a+b
print(a)
