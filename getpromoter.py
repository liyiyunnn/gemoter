#!/usr/bin/env python3

"""
Author: Yiyun Li
Task: get promoter sequences of given genes
"""

from sys import argv

def parse_seq(file_seqs):
    seqs = {} # {"gene":"sequences"}
    lines = open(file_seqs).readlines()
    for line in lines:
        if line.startswith(">"):
            name = line.strip()[1::]
            name = name.split()[0]
            seqs[name] = ""
        else:
            seqs[name] += line.strip()
    return seqs

def get_promoter(file_gene, seqs):
    genes = []
    lines = open(file_gene).readlines()
    for line in lines:
        if line.startswith("AT"):
            gene = line.strip()
            genes.append(gene)
        else:
            raise ValueError("Please check the genelist!")
    select_seq = {}
    for gene in genes:
        if gene in seqs.keys():
            if len(seqs[gene]) == 3000:
                select_seq[gene] = seqs[gene][-1500:]
            else:
                select_seq[gene] = seqs[gene]
        else:
            print(gene,"not found")
    return select_seq

def write_output(select_seq, file_output):
    output = open(file_output, "w")
    for gene, seq in select_seq.items():
        output.write(">")
        output.write(gene)
        output.write("\n")
        output.write(seq)
        output.write("\n")
    output.close()
    return

def main():
    file_seqs = argv[1]
    file_gene = argv[2]
    file_output = argv[3]
    allseqs = parse_seq(file_seqs)
    select_seq = get_promoter(file_gene, allseqs)
    write_output(select_seq, file_output)
    return

if __name__ == '__main__':
    main()