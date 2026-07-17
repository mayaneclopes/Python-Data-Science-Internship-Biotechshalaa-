# Q1. Creating a List ⭐
# Create the following list.
dna_sequences = [
    "ATGCGTAGCTA",
    "GCTAACGTAGC",
    "TTGACCGTAAA",
    "CGTAGGCTAAC",
    "AACCGGTTAAC"
]
# Print:
# Complete list 
# First DNA sequence 
# Last DNA sequence 

print(f"Complete list: {dna_sequences}")
print(f"First DNA sequence: {dna_sequences[0]}")
print(f"Last DNA sequence: {dna_sequences[-1]}")

# Q2. List Indexing ⭐⭐
# Using the same list, print:
# Second DNA sequence 
# Third DNA sequence 
# Fifth DNA sequence 

print(f"Second DNA Sequence: {dna_sequences[1]}")
print(f"Third DNA Sequence: {dna_sequences[2]}")
print(f"Fifth DNA Sequence: {dna_sequences[4]}")

# Q3. List Slicing ⭐⭐
# Using the same list, print:
# First three DNA sequences 
# Last two DNA sequences 
# DNA sequences from index 1 to index 3 

print(f"First 3 DNA sequences: {dna_sequences[:3]}")
print(f"Last 2 DNA sequences: {dna_sequences[-2:]}")
print(f"DNA sequences from inex 1 to index 3: {dna_sequences[1:4]}")

# Q4. Updating a List ⭐⭐⭐
# Create the following list.
genes = [
    "TP53",
    "BRCA1",
    "EGFR",
    "MYC"
]
# Replace:
# "EGFR" with "KRAS" 
# Print the updated list.

genes[2] = "KRAS"
print(genes)

# Q5. Adding New Data ⭐⭐⭐
# Create
patients = [
    "P101",
    "P102",
    "P103"
]
# Perform the following operations.
# Add "P104" using append() 
# Insert "P100" at index 0 
# Print the final list. 

patients.append("P104")
patients.insert(0, "P100")
print(patients)

# Q6. Removing Data ⭐⭐⭐
# Create
genes = [
    "TP53",
    "BRCA1",
    "EGFR",
    "MYC",
    "KRAS"
]
# Remove:
# "EGFR" 
# Print the updated list.

genes.remove("EGFR")
print(genes)

# Q7. String Methods ⭐⭐⭐
# Create
gene = "tp53"

dna = "ATGCGTAGCTA"
# Print:
# Gene after using capitalize() 
# Number of "A" in the DNA sequence 
# Index of the first "G" 
# Length of the DNA sequence 

print(gene.capitalize())
print(dna.count("A"))
print(dna.find("G"))
print(len(dna))

# Q8. Finding the Next Occurrence ⭐⭐⭐⭐
# Create
dna = "ATGCGCTAGCTA"
# Print:
# Index of the first "A" 
# Index of the second "A" using find() 
# (Hint: Use the start parameter.)

print(dna.find("A"))
print(dna.find("A", dna.find("A") + 1))

# Q9. Mutable vs Immutable ⭐⭐⭐⭐
# Run the following program.
dna = "atgcgtagcta"

print(dna.capitalize())
# It prints
# atgcgtagcta
# instead of
# Atgcgtagcta
# Modify the program so that the output becomes
# Atgcgtagcta

# Q10. Patient Records (Nested Lists) ⭐⭐⭐⭐⭐
# Create the following nested list.
patients = [
    ["P101", "Rahul", "ATGCGTAGCTA"],
    ["P102", "Priya", "GCTAACGTAGC"],
    ["P103", "Aman", "TTGACCGTAAA"]
]
# Print:
# Complete information of the first patient. 
# Name of the second patient. 
# DNA sequence of the third patient. 
# First nucleotide of the second patient's DNA sequence. 
# Last nucleotide of the first patient's DNA sequence. 
print(patients[0])
print(patients[1][1])
print(patients[2][2])
print(patients[1][2][0])
print(patients[0][2][-1])


# ⭐ Challenge Question
# A scientist collected DNA sequences from five patients.
dna_sequences = [
    "ATGCGTAGCTA",
    "GCTAACGTAGC",
    "TTGACCGTAAA",
    "CGTAGGCTAAC",
    "AACCGGTTAAC"
]
# Write a program to display the following:
# ========== DNA REPORT ==========

# First DNA Sequence :
# Last DNA Sequence :

# First 5 Nucleotides :
# Last 5 Nucleotides :

# Total DNA Sequences :

# Number of A in First DNA Sequence :

# Index of First G in Last DNA Sequence :

print("============ DNA REPORT ==========")
print(f"First DNA sequence: {dna_sequences[0]}")
print(f"Last DNA sequence: {dna_sequences[-1]}")
print(f"First 5 nucleotides: {dna_sequences[0][:5]}")
print(f"Last 5 nucleotides: {dna_sequences[-1][-5:]}")
print(f"Total DNA Sequecences: {len(dna_sequences)}")
print(f"Number of A in First DNA Sequecence: {dna_sequences[0].count("A")}")
print(f"Index of first G in last DNA sequecene: {dna_sequences[-1].index("G")}")