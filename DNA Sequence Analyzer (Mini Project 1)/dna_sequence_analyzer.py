dna_database = [] #initiating empty db as asked in step 9

while True: #bonus 1 - while loop to get multiple samples
    next_ID = len(dna_database) + 1 #adding a new ID for the next sample
    auto_ID = f"DNA{next_ID:03d}"  #showcasing ID, formatting 3 numbers to the left
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
            "Sequence ID" : auto_ID,
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
        new_dna = input(f"Insert new DNA sample? [Y/N]").lower().strip()
        if new_dna in ['n', 'no']:
            break            
    else: 
        print("Invalid DNA sequence")
        new_dna = input(f"Insert new DNA sample? [Y/N]").lower().strip() #making sure invalid sequences also gets into the loop
        if new_dna in ['n', 'no']:
            break  

for sample in dna_database:
    print("======================================")
    print("     DNA SEQUENCE ANALYSIS REPORT")
    print("======================================")
    print(f"Sequence ID      : {sample['Sequence ID']}")
    print(f"DNA Sequence     : {sample['DNA Sequence']}")
    print(f"Sequence Length  : {sample['Sequence Length']}")
    print(f"A Count          : {sample['A Count']}")
    print(f"T Count          : {sample['T Count']}")
    print(f"G Count          : {sample['G Count']}")
    print(f"C Count          : {sample['C Count']}")
    print(f"Start Codon      : {sample['Start Codon']}")
    print(f"Classification   : {sample['Classification']}")
    print("======================================")