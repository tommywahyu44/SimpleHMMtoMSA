from Bio.Seq import Seq
seq1 = Seq("ACSA")
seq2 = Seq("AST")
seq3 = Seq("ACCST")
hmm1 = Seq("")
hmm1 = hmm1.tomutable()
batas = 4

def kurangDari(seqAwal,seqAkhir):
    y = 0
    for x in range(len(seqAwal)):
        if seqAwal[x] == seqAkhir[y]:
            hmm1.append('M')
            y = y + 1
        elif x + 1 < len(seqAwal):
            if seqAwal[x + 1] == seqAkhir[y]:
                hmm1.append('D')
            else:
                hmm1.append('D')
                hmm1.append('I')
                y = y + 1
        else:
            hmm1.append('M')

def lebihDari(seqAwal,seqAkhir):
    y = 0
    for x in range(len(seqAkhir)):
        if seqAwal[y] == seqAkhir[x]:
            hmm1.append('M')
            y = y + 1
        elif x + 1 < len(seqAkhir):
            if seqAkhir[x + 1] == seqAwal[y]:
                hmm1.append('I')
            else:
                hmm1.append('D')
                hmm1.append('I')
                y = y + 1
        else:
            hmm1.append('M')

def samaDengan(seqAwal,seqAkhir):
    y = 0
    for x in range(len(seqAwal)):
        if seqAwal[x] == seqAkhir[y]:
            hmm1.append('M')
            y = y + 1
        elif x + 1 < len(seqAwal):
            if seqAwal[x + 1] == seqAkhir[y]:
                hmm1.append('I')
                hmm1.append('M')
                hmm1.append('D')
                y = y+2
                x = x+1
            else:
                hmm1.append('D')
                hmm1.append('I')
                y = y + 1
        else:
            hmm1.append('M')


def cekSequence(seqAwal,seqAkhir):
    if len(seqAwal) < len(seqAkhir):
        lebihDari(seqAwal,seqAkhir)
    elif len(seqAwal) > len(seqAkhir):
        kurangDari(seqAwal, seqAkhir)
    else:
        samaDengan(seqAwal, seqAkhir)



cekSequence(seq1,seq1)
for x in range(max(len(seq1),batas)):
    print(hmm1[x],end="")
print("")
cekSequence(seq1,seq2)
for x in range(max(len(seq2),batas)):
    print(hmm1[x+max(len(seq1),batas)],end="")
print("")
cekSequence(seq1,seq3)
for x in range(max(len(seq3),batas)):
    print(hmm1[x+max(len(seq1),batas)+max(len(seq1),batas)],end="")
print("")










