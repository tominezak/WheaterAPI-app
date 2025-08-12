# membership operators = used to test wether a value is found in a sequence (like a list, tuple, or string, dictionary)
# in = returns True if the value is found in the sequence
# not in = returns True if the value is not found in the sequence

# STRING:
word = "apple"

letter = input("guess a letter in the secret word: ")

if letter in word:
    print(f"Good job! The letter '{letter}' is in the word '{word}'.")
else:
    print(f"Sorry, the letter '{letter}' is not in the word '{word}'.")

# SET:

students = {"sponegbob", "patrick", "sandy"}

student = input("Enter a student name: ")

if student in students:
    print(f"{student} is in the class.")
else:
    print(f"{student} is not in the class.")


# DICTIONARY:

grades = {"Sandy": "A", "Patrick": "B", "SpongeBob": "C"}
student = input("Enter a student name to check their grade: ")
if student in grades:
    print(f"{student} has a grade of {grades[student]}.")