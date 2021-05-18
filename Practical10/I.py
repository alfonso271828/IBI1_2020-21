sequence = 'ACTAGTACTGTACTGtacgtcatg'

def reverse_complement_calculator(x):
    """
    calculate the reverse complement of "sequence"

    """
    tem = '' # a string store complementary sequence
    for i in range(0,len(x)): #scan every nucleotide
        if x[i] == 'A' or x[i] == 'a': #change the nucleotide to its complement
             tem = tem + 'T'
        elif x[i] == 'T' or x[i] == 't':
             tem = tem + 'A'
        elif x[i] == 'C' or x[i] == 'c':
             tem = tem + 'G'
        else:
             tem = tem +'C'
    sequence_final = ''
    for i in range(len(tem)-1,-1,-1): # reverse the complementary sequence by reading the string reversely and add the nucleotides into a new string
        sequence_final = sequence_final + tem[i]
    print(sequence_final)
    return

a=reverse_complement_calculator(sequence)
