complentary_gene = {"A": "T", "T": "A", "G": "C", "C": "G"}


def find_gene(dna_sequence: str):
    index = dna_sequence.find("ATG")
    # slice function starting at index to end
    return dna_sequence[index:]


def find_gene_bp(dna_sequence: str):
    return dna_sequence.find("ATG") + 1


def find_upstream(dna_sequence):
    index = dna_sequence.find("ATG")
    # slice function starting at 0 to before "ATG"
    return dna_sequence[:index]


def second_codon(gene_sequence):
    return gene_sequence[3:6]

    # return second codon of gene


def third_codon(gene_sequence):
    return gene_sequence[6:9]


# give single nucleotide, return complement of nucleotide
def complementary_nucleotide(nucleotide):
    return complentary_gene[nucleotide]


def complementary_sequence(dna_sequence):
    complentary_string = ""
    for nucleotide in dna_sequence:
        complentary_string += complementary_nucleotide(nucleotide)
    return complentary_string


def create_double_helix(dna_sequence, comp_sequence):
    plus_strand = ""
    neg_strand = ""
    bar = ""
    for i in range(0, len(dna_sequence)):
        plus_strand += dna_sequence[i]
        bar += "|"
        neg_strand += comp_sequence[i]
    return [plus_strand, bar, neg_strand]


if __name__ == "__main__":
    # MAIN BLOCK
    user_dna_sequence = str(input(f"Please enter a DNA genetic sequence: \n"))
    gene_sequence = find_gene(user_dna_sequence)
    comp_sequence = complementary_sequence(gene_sequence)
    gene_bp = find_gene_bp(user_dna_sequence)
    upstream_sequence = find_upstream(user_dna_sequence)
    double_helix = create_double_helix(gene_sequence, comp_sequence)

    print("Original sequence:", user_dna_sequence)

    print("\nATG codon at bp", gene_bp)
    print(f"    followed by {second_codon(gene_sequence)} at bp", gene_bp + 3)
    print(f"    followed by {third_codon(gene_sequence)} at bp", gene_bp + 6)

    print("\nUpstream sequence:", upstream_sequence)
    print("Upstream length:  ", len(upstream_sequence), "bp")
    print("\nGene sequence:", gene_sequence)
    print("Gene length:  ", len(gene_sequence), "bp")
    print("[+ Strand]:", double_helix[0])
    print("           ", double_helix[1])
    print("[- Strand]:", double_helix[2])
