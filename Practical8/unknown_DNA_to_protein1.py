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
N =re.findall('\d\n([A-Z]+)',s)

T =[]
for i in range(len(N)):
    b=N[i]
    translation =''
    for a in range(0,len(b),3):
        if Condons[b[a:a + 3]] !=('O'or'U'or'X'):
                  translation = translation + Condons[b[a:a + 3]]
        else:
            break
    T.append(translation)
lengths = []
for z in range(len(T)):
    lengths.append(len(T[z]))
M=re.findall('([0-9A-Z]+?)\s+?[0-9]+?',s)
new = open('unknown_DNA_to_protein2.fa','w')
for q in range(len(N)):
    new.write(f'{M[q]:16}{lengths[q]}\n{T[q]}\n')
new.close()
new1 = open('unknown_DNA_to_protein2.fa')
for line in new1:
    print(line[:-1])



