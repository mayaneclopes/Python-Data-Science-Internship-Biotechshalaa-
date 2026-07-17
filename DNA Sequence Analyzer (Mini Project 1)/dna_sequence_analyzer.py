dna = input("Type the DNA sequence: ").upper() #creating user input
print(dna)

is_valid = True #Initiating validation variable

for nucleotideo in dna: #validation through a for loop
    if nucleotideo not in "ATGC": 
        is_valid = False
        break #once the 1st invalid char is found, the loop is finished

if is_valid:  
    print("Valid DNA sequence")
else: 
    print("Invalid DNA sequence")

#initializing counters
counter_A = 0
counter_T = 0
counter_G = 0
counter_C = 0

for nucleotideo in dna:
    if nucleotideo == "A":
        counter_A += 1
    elif nucleotideo == "T":
        counter_T += 1
    elif nucleotideo == "G":
        counter_G += 1
    elif nucleotideo == "C":
        counter_C += 1
    else:
        break

print(f"A = {counter_A}")
print(f"T = {counter_T}")
print(f"G = {counter_G}")
print(f"C = {counter_C}")