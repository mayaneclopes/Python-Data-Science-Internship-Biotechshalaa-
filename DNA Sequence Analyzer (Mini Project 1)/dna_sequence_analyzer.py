dna = input("Type the DNA sequence: ").upper() #creating user input
print(dna)

is_valid = True #Initiating validation variable

for nucleotideo in dna: #validation through a for loop
    if nucleotideo not in "ATGC": 
        is_valid = False
        break #once the 1st invalid char is found, the loop is finished

if is_valid:  
    print("Valid DNA sequence")

    #initializing counters inside if/else to ensure it wont count invalid sequences
    counter_A = dna.count("A")
    counter_T = dna.count("T")
    counter_G = dna.count("G")
    counter_C = dna.count("C")

    print(f"Total DNA lenght: {len(dna)}")
    if len(dna) >= 10:
        print("Long DNA Sequence")
    else:
        print("Short DNA Sequence")
    print(f"A = {counter_A}")
    print(f"T = {counter_T}")
    print(f"G = {counter_G}")
    print(f"C = {counter_C}")

    start_codon = "ATG"
    if start_codon in dna:
        print(f"Start Codon found in position {dna.find("ATG") + 1}")
    else:
        print("Start Codon Not Found")

else: 
    print("Invalid DNA sequence")

