#define r and original n
#calculate the increase of infected person by a=a*r
#sum n and each a
n=84
a=n
r=1.2
for i in range (1,6):
    a=a*r
    n=n+a
print("When r =", r ,"n=",n,"after 5 generations")
