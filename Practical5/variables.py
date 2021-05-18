a = 170702 #my birthday
c = 100321 #date
d = abs(a-c)
e = abs(a-190784)
if d<e:
    print("d<e")
elif d==e:
    print("d=e")
else:
    print("d>e")
X= True
Y= False
Z= (X and not Y)or (Y and not X)
W= (X!=Y)
print (W)
print (Z)

