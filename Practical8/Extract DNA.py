import re
S = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
s = S.read()
s = ''.join(s.split('\n'))
s = s.replace('\n','') # change the file into a string with a single line
N = re.findall('gene:(\S+).+?unknown function',s)#extract the name of gene with unknown function
M = re.findall(r'unknown function.+?](.+?)>',s)#extract sequence by 'unknown function'
lengths = [] # a list store lengths of each sequence
for i in range(len(M)):
    lengths.append(len(M[i])) # count the lengths and add it to the list
new = open('unknown_function.fa','w') # creat a file to store the result
for i in range(len(N)):
    new.write(f'{N[i]:16}{lengths[i]}\n{M[i]}\n')#combine everything and write them in the file
new.close()
new1 = open('unknown_function.fa')
for line in new1:# print the file
    print(line[:-1])