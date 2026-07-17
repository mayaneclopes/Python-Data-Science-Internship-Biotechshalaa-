dna_database = [] #initiating empty db as asked in step 9
dna = input("Type the DNA sequence: ").upper() #creating user input

is_valid = True #Initiating validation variable

for nucleotideo in dna: #validation through a for loop
    if nucleotideo not in "ATGC": 
        is_valid = False
        break #once the 1st invalid char is found, the loop is finished

if is_valid:  

    #initializing counters inside if/else to ensure it wont count invalid sequences
    counter_A = dna.count("A")
    counter_T = dna.count("T")
    counter_G = dna.count("G")
    counter_C = dna.count("C")

    sequence_analysis = { #creating dic
        "Sequence ID" : "",
        "DNA Sequence": dna,
        "Sequence Length": len(dna),
        "Classification": "Long DNA Sequence" if len(dna) >= 10 else "Short DNA Sequence",
        "A Count": counter_A,
        "T Count": counter_T,
        "G Count": counter_G,
        "C Count": counter_C,
        "Start Codon": f"Start Codon Found in position {dna.find('ATG') + 1}" if "ATG" in dna else "Start Codon Not Found"
    }
    dna_database.append(sequence_analysis) #adding to db
else: 
    print("Invalid DNA sequence")

print("======================================")
print("     DNA SEQUENCE ANALYSIS REPORT")
print("======================================")
print(f"Sequence ID      : {sequence_analysis['Sequence ID']}")
print(f"DNA Sequence     : {sequence_analysis['DNA Sequence']}")
print(f"Sequence Length  : {sequence_analysis['Sequence Length']}")
print(f"A Count          : {sequence_analysis['A Count']}")
print(f"T Count          : {sequence_analysis['T Count']}")
print(f"G Count          : {sequence_analysis['G Count']}")
print(f"C Count          : {sequence_analysis['C Count']}")
print(f"Start Codon      : {sequence_analysis['Start Codon']}")
print(f"Classification   : {sequence_analysis['Classification']}")
print("======================================")