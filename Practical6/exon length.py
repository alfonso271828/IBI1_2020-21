import matplotlib.pyplot as plt
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]# list of gene lengths
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]# list of exon counts
average_length=[]#creat a list for average length
for i in range(len(gene_lengths)):
    average_length.append(gene_lengths[i] / exon_counts[i]) #calculate the average length of 10 genes
average_length.sort()#sort the list
print(average_length)
plt.boxplot(average_length,#draw a boxplot
            vert = True,
            whis=  1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showfliers = True,
            notch = False
            )
plt.show()