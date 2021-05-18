# What does this piece of code do?
# Answer: get a random number that is lower than 50

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False: # run this code until it generate a number less than 50.
	n = randint(1,100) #generate random number from 1-100
	if n > 50:
		p = False # if the number is larger than 50, keep running

print(n)