sequence = 'ACTAGTACTGTACTGtacgtcatg'

def reverse_complement_calculator(x):
    """
    calculate the reverse complement of "sequence"

    """
    tem = ''
    for i in range(0,len(x)):
        if x[i] == 'A' or x[i] == 'a':
             tem = tem + 'T'
        elif x[i] == 'T' or x[i] == 't':
             tem = tem + 'A'
        elif x[i] == 'C' or x[i] == 'c':
             tem = tem + 'G'
        else:
             tem = tem +'C'
    sequence_final = ''
    for i in range(0,len(tem)):
        sequence_final = sequence_final + tem[len(tem)-1-i]
    print(sequence_final)
    return

a=reverse_complement_calculator(sequence)