nucleotides = "ATCG" #allowed caracthers 

dna_sequence = input("Type the DNA sequence: ").upper() #creating user input

validation = all(char in nucleotides for char in dna_sequence)
print(validation)