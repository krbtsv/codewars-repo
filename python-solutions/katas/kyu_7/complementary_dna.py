def dna_strand(dna):
    sides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([sides[symbol] for symbol in dna])


def dna_strand_second_solution(dna):
    my_dict = {65: 84, 84: 65, 67: 71, 71: 67}
    return dna.translate(my_dict)
