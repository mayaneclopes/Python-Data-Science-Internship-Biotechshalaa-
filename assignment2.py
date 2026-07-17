# Question 1 – Biological Sample Registration (User Input)
# A laboratory technician wants to register a DNA sample.
# Write a Python program that asks the user to enter:
#  Sample ID
#  Patient Name
#  Age
#  Species Name
#  Gene Name
#  DNA Sequence
# Display the output in the following format.
# ========== SAMPLE DETAILS ==========
# Sample ID :
# Patient Name :
# Age :
# Species Name :
# Gene Name :
# DNA Sequence :
# ===================================

ident = input("Enter the Sample's ID: ")
name = input("Enter the patients's name: ")
age = input("Enter the patient's age: ")
species = input("Enter the species: ")
gene = input("Enter gene's name: ")
dna_seq = input("Enter DNA sequence: ")

print("======== SAMPLE DETAILS ==========")
print(f"Sample ID: {ident}")
print(f"Patient Name: {name}")
print(f"Age: {age}")
print(f"Species Name: {species}")
print(f"Gene Name: {gene}")
print(f"DNA Sequence: {dna_seq}")
print("==================================")

# Question 2 – Gene Expression Analysis
# A researcher measured the expression level of two genes.
gene_A = 125
gene_B = 80
# # Write a Python program to display:
# #  Total Expression
total = gene_A + gene_B
print(f"Total expression: {total}")
# #  Difference
difference = gene_A - gene_B
print(f"Difference: {difference}")
# #  Product
product = gene_A * gene_B
print(f"Product: {product}")
# #  Division
division = gene_A / gene_B
print(f"Division: {division}")
# #  Floor Division
floor_div = gene_A // gene_B
print(f"Floor division: {floor_div}")
# #  Modulus
modulus = gene_A % gene_B
print(f"Modulus = {modulus}")
# #  Square of Gene A Expression
square = gene_A ** 2
print(f"Square of Gene A: {square}")

# Question 3 – Clinical Trial Eligibility
# The following information is available.
patient_name = "Rahul"
age = 20
temperature = 37.5
# Write a Python program to display the output of the following conditions.
# age >= 18
# temperature <38
# age >=18 and temperature >38
# age >=18 or temperature >38
# not(age>=18)

print(f"Condition 1 (age greater or equal to 18): ", age >= 18)
print(f"Condition 2 (temperature lower than 38): ", temperature < 38)
print(f"Condition 3 (age greater or equal to 18 and temperature greater than 38)", age >= 18 and temperature < 38)
print(f"Condition 4 (age greater or equal to 18 or temperature greater than 38):", age >= 18 or temperature > 38)
print(f"Condition 5 (age not equal or greater than 18):", not(age>=18))

# Question 4 – DNA Indexing Challenge
# The following DNA sequence belongs to a patient.
dna = "ATGCGTAGCTA"
# Write a Python program to display:
#  First nucleotide
#  Third nucleotide
#  Fifth nucleotide
#  Last nucleotide
#  Third nucleotide from the end
print(f"First nucleotide: {dna[0]}")
print(f"Third nucleotide: {dna[2]}")
print(f"fifth nucleotide: {dna[4]}")
print(f"Last nucleotide: {dna[-1]}")
print(f"Third nucleotide from the end: {dna[-3]}")

# Question 5 – Protein Sequence Analysis
# A protein sequence is given below.
protein = "MKWVTFISLLFLFSSAYS"
# Write a Python program to display:
#  First amino acid
#  Fourth amino acid
#  Last amino acid
#  Fifth amino acid from the end

print(f"First amino acid: {protein[0]}")
print(f"Fourth amino acid: {protein[3]}")
print(f"Last amino acid: {protein[-1]}")
print(f"Fifth amino acid from the end: {protein[-5]}")      

# Question 6 – DNA Fragment Extraction
# A scientist wants to study different regions of the DNA sequence.
dna = "ATGCGTAGCTAACGT"
# Write a Python program to display:
#  First 6 nucleotides
#  Last 6 nucleotides
#  Nucleotides from index 3 to 9
#  Everything after index 5
#  Everything except the last nucleotide
print(f"First 6 nucleotides: {dna[0:6]}")
print(f"Last 6 nucleotides: {dna[-6:]}")
print(f"Nucleotides from index 3 to 9: {dna[3:10]}")
print(f"Everything after index 5: {dna[6:]}")
print(f"Everything except the last nucleotide: {dna[:-1]}")

# Question 7 – Step Slicing Challenge
# The following DNA sequence is obtained after sequencing.
dna = "GCTATCGGAATCGTAG"
# Write a Python program to display:
#  Every second nucleotide
#  Every third nucleotide
#  Every second nucleotide starting from index 1
#  Every third nucleotide starting from index 2
#  Reverse DNA sequence
print(f"Every second nucleotide: {dna[::2]}")
print(f"Every third nucleotide: {dna[::3]}")
print(f"Every second nucleotide starting from index 1: {dna[1::2]}")
print(f"Every third nucleotide starting fron index 2: {dna[2::3]}")
print(f"Reverse DNA sequence: {dna[::-1]}")

# Question 8 – Debug the Program
# The following program gives an error.
# dna = "ATGCGTAGCTA"
# print(dna[20])
# 1. Run the program.
# 2. Identify the error.
# 3. Correct the program so that it prints the last nucleotide of the DNA sequence.

#answer: 
dna = "ATGCGTAGCTA"
print(dna[-1])

# Question 9 – Predict the Output
# Without running the program, write the expected output as comments.
# Then execute the program and check your answers.
dna = "ATCGGCTAAG"
print(dna[0])
print(dna[-3])
print(dna[2:8])
print(dna[:6])
print(dna[4:])
print(dna[::2])
print(dna[::-1])
# Example:
# # Expected Output:
# # A
# # A
# # CGGCTA
# # ATCGGC
# # GCTAAG
# # ACGTA
# # GAATCGGCTA

# Question 10 – DNA Sequence Report (Mini Challenge)
# A scientist provides the following DNA sequence.
sample_id = "S205"
species = "Homo sapiens"
gene = "BRCA1"
dna = "ATGCGTAGCTAACGTAGCTA"
# Write one Python program that generates the following report.
# ========== DNA REPORT ==========
# Sample ID :
# Species :
# Gene :
# Complete DNA Sequence :
# First Nucleotide :
# Last Nucleotide :
# First 8 Nucleotides :
# Last 8 Nucleotides :
# Every Second Nucleotide :
# Reverse DNA Sequence :
# ===============================

print("========= DNA REPORT ============")
print(f"Sample ID: {sample_id}")
print(f"Species: {species}")
print(f"Gene: {gene}")
print(f"Comple DNA Sequence: {dna}")
print(f"First nucleotide: {dna[0]}")
print(f"Last Nucleotide: {dna[-1]}")
print(f"First 8 nucleotides: {dna[:8]}")
print(f"Last 8 nucleotides: {dna[-8:]}")
print(f"Every second nucleotidE: {dna[::2]}")
print(f"Reverse DNA sequence: {dna[::-1]}")
print("================================")