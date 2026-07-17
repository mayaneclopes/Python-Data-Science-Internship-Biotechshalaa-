🧬 Mini Project 1
DNA Sequence Analyzer
Python & Data Science Program (Biotechshalaa)

📖 Project Background
Imagine you have joined a Bioinformatics laboratory as an intern.
Researchers generate DNA sequences every day from different biological samples.
Before these DNA sequences can be used for downstream analyses such as Sequence Alignment, BLAST, Variant Calling, or Genome Analysis, they must first be checked for correctness and basic statistics must be calculated.
Your task is to build a simple DNA Sequence Analyzer that performs these initial quality checks.
The purpose of this project is to apply all the Python concepts you have learned so far to build a real-world bioinformatics application.

🎯 Project Objective
Develop a Python program that:
Accepts a DNA sequence from the user. 
Validates whether it is a correct DNA sequence. 
Performs basic sequence analysis. 
Displays a professional analysis report. 
Stores the analysis for future reference. 

📌 Project Workflow
User Enters DNA Sequence
            │
            ▼
Convert to Uppercase
            │
            ▼
Validate DNA Sequence
            │
            ▼
Calculate Sequence Statistics
            │
            ▼
Generate DNA Analysis Report
            │
            ▼
Store Analysis in a Database (List)

✅ Step 1 — Accept DNA Sequence
Ask the user to enter a DNA sequence.
Example
Enter DNA Sequence:
ATGCGTAGCTA
Hint
Use
input()
Store the sequence in a variable named
dna

✅ Step 2 — Standardize the Sequence
The user may enter
atgcgtagcta
or
AtGcGTAGcTa
Convert the sequence into uppercase before starting the analysis.
Hint
Think about which string method converts all letters to uppercase.

✅ Step 3 — Validate the DNA Sequence
A valid DNA sequence contains only
A
T
G
C
Check every nucleotide using a for loop.
If any character other than A, T, G, or C is found,
display
Invalid DNA Sequence
Otherwise display
Valid DNA Sequence
Example
Input
ATGXGT
Output
Invalid DNA Sequence
Hint
Think about
if nucleotide not in "ATGC":

✅ Step 4 — Calculate DNA Sequence Length
Display the total number of nucleotides.
Example
Sequence Length : 11 nucleotides
Hint
Which function returns the length of a string?

✅ Step 5 — Calculate Nucleotide Composition
Count how many times each nucleotide appears.
Display
A : 3

T : 3

G : 3

C : 2
This is called Nucleotide Composition, which is one of the first analyses performed on DNA sequences.
Hint
Think about which string method counts characters.

✅ Step 6 — Detect the Start Codon
Check whether the DNA sequence contains
ATG
If found,
display
Start Codon Found
Otherwise,
display
Start Codon Not Found
Bonus
Also display the position where it was found.
Hint
Which string method searches for a substring inside another string?

✅ Step 7 — Classify the DNA Sequence
Use a conditional statement.
If the DNA sequence contains 10 or more nucleotides, display
Long DNA Sequence
Otherwise display
Short DNA Sequence

✅ Step 8 — Store the Analysis in a Dictionary
Create a dictionary to store the results of your analysis.
Example keys
Sequence ID

DNA Sequence

Status

Sequence Length

A Count

T Count

G Count

C Count

Start Codon
Your dictionary should store all the information generated during the analysis.
Example Structure
sequence_analysis = {

}

✅ Step 9 — Create a DNA Database
Scientists analyze many DNA sequences, not just one.
Create a list named
dna_database = []
Store your dictionary inside this list.
Your list will act as a small DNA sequence database.
Hint
Think about the list method used to add a new element.

✅ Step 10 — Display the Final Analysis Report
Display the results in a clean and professional format.
Example
======================================

        DNA SEQUENCE ANALYSIS REPORT

======================================

Sequence ID      : DNA001

DNA Sequence     : ATGCGTAGCTA

Status           : Valid DNA Sequence

Sequence Length  : 11 nucleotides

Nucleotide Composition

A : 3
T : 3
G : 3
C : 2

Start Codon      : Found

Classification   : Long DNA Sequence

======================================
Try to make your report easy to read.

🌟 Bonus Features (Optional)
If you complete the project early, you may add one or more of these features.
⭐ Bonus 1 — Analyze Multiple DNA Sequences
After analyzing one sequence, ask the user
Do you want to analyze another DNA sequence?

Yes / No
Use a while loop to repeat the program until the user enters No.

⭐ Bonus 2 — Store Multiple DNA Analyses
Every time a new sequence is analyzed,
store its dictionary inside the same list.
Example
dna_database

↓

Sequence 1

Sequence 2

Sequence 3

⭐ Bonus 3 — Display All DNA Reports
Use a for loop to display every DNA sequence stored in your database.

⭐ Bonus 4 — Generate Automatic Sequence IDs
Instead of asking the user,
automatically create IDs like
DNA001

DNA002

DNA003

💡 Concepts You Should Use
Try to include as many concepts as possible.
✅ Variables
✅ User Input
✅ Data Types
✅ Strings
✅ String Methods
✅ Lists
✅ Dictionaries
✅ Conditional Statements
✅ Type Conversion (if required)
✅ Operators
✅ For Loop
✅ While Loop

📋 Submission Guidelines
Submit only one Python (.py) file. 
Your program should run without any errors. 
Use meaningful variable names. 
Keep your output clean and readable. 
Write your own code and make sure you understand every line before submitting. 

🏆 Project Evaluation (50 Marks)
Criteria
Marks
Program runs correctly
10
Correct use of Python concepts
10
DNA validation logic
10
Code readability and formatting
10
Overall project design
10


🎯 Final Advice
Don't try to write the entire program at once.
Build it step by step:
Take the DNA sequence as input. 
Convert it to uppercase. 
Validate the sequence. 
Calculate the sequence length. 
Count the nucleotides. 
Detect the start codon. 
Classify the sequence. 
Store the analysis in a dictionary. 
Store the dictionary in a list. 
Display the final report. 
Run your program after completing each step. This is how professional programmers build software—one working feature at a time, rather than writing everything together and debugging at the end.
