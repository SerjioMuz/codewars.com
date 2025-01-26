def DNA_strand(dna):
    #L={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[i] for i in dna])








res = DNA_strand('GTAT')
print(res)