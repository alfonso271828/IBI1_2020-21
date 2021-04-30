import re
S = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
s = S.read()
s = ''.join(s.split('\n'))
s = s.replace('\n','')
N = re.findall('gene:(\S+).+?unknown function',s)#name
M = re.findall(r'unknown function.+?](.+?)>',s)#sequence
lengths = []
for i in range(len(M)):
    lengths.append(len(M[i]))#count the lengths
new = open('unknown_function.fa','w')
for i in range(len(N)):
    new.write(f'{N[i]:16}{lengths[i]}\n{M[i]}\n')#combine everything
new.close()
new1 = open('unknown_function.fa')
for line in new1:
    print(line[:-1])