# Q1.
# Print numbers from 1 to 10 using a for loop.
# Expected Output:
# 1
# 2
# 3
# ...
# 

for x in range(1, 11):
    print(x)

# Q2.
# Print numbers from 10 to 1 using a for loop.
# Expected Output:
# 10
# 9
# 8
# ...
# 1

for x in range(10,0,-1):
    print(x)

# Q3.
# Print all even numbers from 1 to 20.
# Expected Output:
# 2
# 4
# 6
# ...
# 20

for x in range(2,21,2):
    print(x)

# Q4.
# Print all odd numbers from 1 to 20.
# Expected Output:
# 1
# 3
# 5
# ...
# 19

for x in range(1,21,2):
    print(x)

# Q5.
# Given the DNA sequence:
dna = "ATGCGTAGCTA"
# Print each nucleotide on a new line using a for loop.
# Expected Output:
# A
# T
# G
# C
# ...

for nucleotideo in dna:
    print(nucleotideo)

# Q6.
# Given the list:
genes = ["TP53", "BRCA1", "EGFR", "MYC"]
# Print each gene name using a for loop.
for gene in genes:
    print(gene)

# Q7.
# Count how many times A appears in the DNA sequence.
dna = "ATGCGTAGCTA"
# Expected Output:
# 3
# (Do not use .count() method. Use a for loop.)

counter = 0

for nucleotideo in dna:
    if nucleotideo == "A":
        counter += 1

print(counter)

# Q8.
# Count how many G nucleotides are present in the DNA sequence.
dna = "ATGCGTAGCTA"

counter = 0

for nucleotideo in dna:
    if nucleotideo == "G":
        counter += 1

print(counter)

# Q9.
# Print only the vowels from the following string.
name = "Bioinformatics"
# Expected Output:
# i
# o
# i
# o
# a
# i

for vowels in name:
    if vowels in "aeiou":
        print(vowels)
    
# Q10. ★ Homework (Given in Class)
# Print all even numbers from 1 to 20 using a for loop and the % (modulus) operator.
for x in range(1,21):
    if x % 2 == 0:
        print(x)


# Q11. ★ Homework (Given in Class)
# Check whether the DNA sequence is valid.
dna = "ATGXGT"
# Print:
# Invalid DNA sequence
# if any character other than A, T, G, or C is present.
# Explain the complete program

is_valid = True #variable stating the DNA is valid

for nucleotideo in dna: 
    if nucleotideo not in "ATGC": #Chances bool variable to False if find other letter than ATGC 
        is_valid = False
        break #Once we find 1 error, we do not need to check the rest in this situation

if is_valid:  #check if final state of bool is true or false and prints the right answer
    print("Valid DNA sequence")
else: 
    print("Invalid DNA sequence")

# Challenge Question ★★★
# Given:
dna = "ATGCGTAGCTA"
# Count how many times each nucleotide appears and print the result like this:
# A = 3
# T = 3
# G = 3
# C = 2
# (Do not use the .count() method.)

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
        print("Invalid DNA sequence")
        break

print(f"A = {counter_A}")
print(f"T = {counter_T}")
print(f"G = {counter_G}")
print(f"C = {counter_C}")