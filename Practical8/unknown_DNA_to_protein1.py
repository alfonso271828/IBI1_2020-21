import re
Condons ={'TTT':'F','TTC':'F','TTA':'L','TTG':'L','TCT':'S','TCC':'S','TCA':'S','TCG':'S',
          'TAT':'Y','TAC':'Y','TAA':'O','TAG':'U','TGT':'C','TGC':'C','TGA':'X','TGG':'W',
          'CTT':'L','CTC':'L','CTA':'L','CTG':'L','CCT':'P','CCC':'P','CCA':'P','CCG':'P',
          'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z','CGT':'R','CGC':'R','CGA':'R','CGG':'R',
          'ATT':'I','ATC':'I','ATA':'J','ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T',
          'AAT':'N','AAC':'B','AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R',
          'GTT':'V','GTC':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A',
          'GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
S = open('unknown_function.fa')
s = S.read()
N =re.findall('\d\n([A-Z]+)',s) # extract all the sequences

T =[] # a list storing translated sequence
for i in range(len(N)): # to every sequence
    b=N[i]
    translation =''
    for a in range(0,len(b),3): #read the sequence in unit of three
        if Condons[b[a:a + 3]] !=('O'or'U'or'X'):
                  translation = translation + Condons[b[a:a + 3]]# translate the unit in to amino acid and store it in the translated string before stop codon
        else:
            break # break the translation at stop codon
    T.append(translation)
lengths = [] # calculate the length of each translated sequence
for z in range(len(T)): # store the lengths into a list
    lengths.append(len(T[z]))
M=re.findall('([0-9A-Z]+?)\s+?[0-9]+?',s) # extract all names of genes
new = open('unknown_DNA_to_protein2.fa','w') # create a file
for q in range(len(N)):
    new.write(f'{M[q]:16}{lengths[q]}\n{T[q]}\n')# write information of translated sequence into the file
new.close()
new1 = open('unknown_DNA_to_protein2.fa')
for line in new1: #print the file
    print(line[:-1])



