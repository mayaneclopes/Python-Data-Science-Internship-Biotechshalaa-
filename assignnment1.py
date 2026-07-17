# Q1. Write a Python program to print the following exactly as shown:
# ********** Student Information **********
# Name : Muskan
# Age : 23
# Course : M.Sc Biotechnology
# College : XYZ University
# ***************************************
# (Tests: print formatting)

name = "Muskan"
age = 23
course = "M.Sc Biotechnology"
college = "XYZ University"

print(f"Name : {name}")
print(f"Age : {age}")
print(f"Course : {course}") 
print(f"College : {college}")

# Q2. Create variables for the following information and print the output exactly as
# shown.
#  Name
#  Age
#  CGPA
#  Is_Student
#  Gene
#  Species
# Also print the data type of each variable using type().
# (Tests: Variables + Data Types + type())

name = "John Doe"
age = 30
cgpa = 10.0
Is_Student = True 
gene = "BRCA1"
species = "Human"

print(f"Name: {name} \nType of name: {type(name)}")
print(f"Age: {age} \n Type of age {type(age)}")
print(f"CGPA: {cgpa} \n Type of CGPA: {type(cgpa)}")
print(f"Is a student? {Is_Student} \n Type of is_student: {type(Is_Student)}")
print(f"Gene: {gene} \n Type of gene: {type(gene)}")
print(f"Species: {species} \n Type of species: {type(species)}")

# Q3. Predict the output before running the code. Then execute it and verify your
# answer.
name = "Python";
print(name)
name = "BiotechShalaa";
print(name)

# (Tests: Understanding of variable reassignment.)

# Answer: it will show "Python" and then the variable'll be changed to "BiotechShalaa" and it will print that.

# Q4. Predict the output.
gene = "TP53";
print(gene)
gene = "BRCA1";
print(gene)
print(type(gene))

# Answer: it'll print "TP53" and then reassign the variable to "BRCA1", print this and than print that the data type is string.

# Q5. The following program contains errors.
#  Identify the line containing the error.
#  Mention the type of error.
#  Rewrite the correct program.
# Print("Hello")
# gene = TP53
# print(Gene)
# print(species)

#Answers: print function should be written in lowercase, variable gene is missing quotes, the printing of gene should be lowercase, 
#as the variable was written that way, the print of species won't happen as this variable was not written. Corrected verion:

print("Hello")
gene = "TP53"
species = "Human"
print(gene)
print(species)

# Q6. Which of the following variable names are valid in Python? If invalid, explain
# why.
# gene_name
# GeneName
# 2gene
# gene-name
# gene2
# DNA_Sequence
# class
# sample_id
# patientName

#answer: 2gene is invalid as it starts with a number, gene-name is invalid because it uses hifen instead of underscore,
#class is invalid because it is a Python keyword,

# Q7. What will be the output?
# a = 10
# b = 20
# print(a)
# print(b)
# a = b
# print(a)

#Answer: Output will be "10", "20", "20".

# Q8. Debug the following program.
# # Student Details
# name = "Rahul";
# Age = 22
# college = "ABC University";
# Print(name)
# print(age)
# print(college)

# Make the program execute successfully.

# Student Details
name = "Rahul"
age = 22
college = "ABC University"
print(name)
print(age)
print(college)


# Q9. Write a Python program using comments to explain every line of your code.
# The program should contain:
#  At least 5 variables
#  At least 5 comments
#  At least 5 print() statements
# (Tests whether you actually understood comments.)

#Definition of different variables with different data types
name = "Mayane" 
age = 39
is_Intern = True
objective = "Become bioinformatician"
grade = 9.9
find = "Linkedin"

print(f"Name: {name} \n Age: {age}") #Showing name and age of a student in different lines
print(f"Is this student an intern? {is_Intern}") #Showcasing boolean value that states if student is an intern or not
print(f"What is the student's objective? {objective}") #Returning string value of student's objectives
print(f"What is their grade? {grade}") #Showcasing float value 
print(f"Where did they find the program? {find}") #Showcasing student's answer for the question


# Q10. Challenge Question ⭐⭐⭐
# Without using Google or ChatGPT,
# write a Python program that displays the following:
# Student Details
# -------------------------
# Name :
# Age :
# Species :
# Gene :
# DNA Sequence :
# Data Types
# -------------------------
# Name :
# Age :
# Species :
# Gene :
# DNA Sequence :

name = "Muskan"
age = 23
gene = "TP53"
species = "Human"
dna_sequence = "ATCGGCTA"
gene = "BRCA1"

print(f"Name : {name}")
print(f"Age : {age}")
print(f"Species : {species}")
print(f"Gene : {gene}")
print(f"DNA Sequence : {dna_sequence}")
print(f"Data Types:")
print(f"---------------")
print(f"Name : {type(name)}")
print(f"Age : {type(age)}")
print(f"Species : {type(species)}")
print(f"Gene : {type(gene)}")
print(f"DNA Sequence : {dna_sequence}")