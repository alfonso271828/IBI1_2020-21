# It might takes around 5 minutes to run this code, because go_obo.xml provided was quite big.
import re
import matplotlib.pyplot as plt
from xml.dom.minidom import parse
import xml.dom.minidom
go_obo = open('go_obo.xml','r')
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')
ids = [0]*1000000000 #create a list matching id and term index
index_of_term = 0 #initiate the index of term
for term in terms:
    id = term.getElementsByTagName('id')[0].childNodes[0].data #extract id of that term
    N = re.findall('\d.+',id)
    n = int(N[0])#extract id and turn it into number
    ids[n] = index_of_term #store index of the term into 'ids' at index = id
    index_of_term = index_of_term + 1
def find_related(info,term): #find the parent concept of a concept and check if it has DNA/RNA/... in 'defstr'
    is_a = term.getElementsByTagName('is_a')
    flag = False
    if is_a ==[]:
        flag = False #if this concept doesn't have a parent concept, return False
    else:
        for a in is_a:
            ID=a.childNodes[0].data
            Num = re.findall('\d.+',ID)
            num = int(Num[0]) #extract id of its parent concept in 'is_a'
            t= terms[ids[num]] # match the id of parent with parent term
            defstr=t.getElementsByTagName('defstr')[0]
            d=defstr.childNodes[0].data# extract defstr
            if re.search(info,d):# check if defstr has DNA/RNA/...
                flag = True
            elif find_related(info,t):# if parent defstr doesn't have DNA/RNA/... search parent of the parent...
                flag = True
    return flag
count=0
DNA = 0
RNA = 0
protein = 0
carbohydrate = 0
for term in terms:#check every concept to see if one of its upper concepts have DNA
    if find_related('DNA',term):#count the number of DNA related
        DNA = DNA+1
print('DNA related: ',DNA)
for term in terms:
    if find_related('RNA',term):
        RNA = RNA+1
print('RNA related: ',RNA)
for term in terms:
    if find_related('protein',term):
        protein = protein+1
print('protein related :', protein)
for term in terms:
    if find_related('carbohydrate',term):
        carbohydrate = carbohydrate+1
print('carbohydrate related: ', carbohydrate)
sizes = [DNA,RNA,protein,carbohydrate]
labels = ['DNA related','RNA related','protein related','carbohydrate related']
plt.pie(sizes, explode=None, labels=labels,
    colors=('b', 'r', 'g', 'c'),
    autopct='%1.2f%%', pctdistance=0.6, shadow=True,
    labeldistance=1.1, startangle=0, radius=1,
    counterclock=True, wedgeprops=None, textprops=None,
    center = (0, 0), frame = False )
plt.title('Amount of related concepts')
plt.axis('equal')
plt.show()