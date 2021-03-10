#define r and original n
#calculate n after one genera by n*(r+1)
#repete in total 5 times
n=84
r=1.2
for i in range (1,6):
    n=n*(r+1)

print("When r =", r ,"n=",n,"after 5 generations")