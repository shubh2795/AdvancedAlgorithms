

path = ""
fileName = "covid_DNA.fasta"

def read_fasta(howMany=10):
    # The first line in a FASTA record is the title line.
    # Examples:
    # >third sequence record
    # >gi|2765657|emb|Z78532.1|CCZ78532 C.californicum 5.8S rRNA gene
    # returns a list of sequences as tuples (name.)
    with open(path + fileName, 'r') as filePt:
        sequences = []
        fastas = filePt.read().split(">")
        fastas = fastas[1:]
        for i in range(0, howMany):
            seq = fastas[i].split("\n")
            seq_name = seq[0]
            fasta_seq = "".join(seq[1:])
            sequences.append((fasta_seq))
        x = sequences
    # create a text file with all sequences separated by "\n" and copy themy to sequences to use them as global.
    f = open("seq.txt", "w")
    for i in range(len(x)):
        f.write(x[i] + "\n")

    f.close()



