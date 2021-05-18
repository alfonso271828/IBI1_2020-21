#define r and original n
#calculate the increase of infected person by a=a*r
#sum n and each a
n=84
a=n
r=1.2 #define r
for i in range (1,6): #run 5 generations
    a=a*r # the number of person infected this generation
    n=n+a # add the number of person infected this generation to total infections
print("When r =", r ,", ","n=",n,"after 5 generations.")
