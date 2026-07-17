dna_database = [] #initiating empty db as asked in step 9
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

    sequence_analysis = {
        "Sequence ID" : "",
        "DNA Sequence": dna,
        "Sequence Length": len(dna),
        "A Count:": counter_A,
        "T Count:": counter_T,
        "G Count:": counter_G,
        "C count:": counter_C,
        "Start Codon:": f"Start Codon Found in position {dna.find("ATG") + 1}"
        if "ATG" in dna else "Start Codon Not Found"
    }
    dna_database.append(sequence_analysis)
    print(sequence_analysis)
else: 
    print("Invalid DNA sequence")

