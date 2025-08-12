# Iterables = an object that can return one of its elements at a time, allowing it to be iterated over in a loop.

# obs man man kan ikke bruke reversed på set lister

name = "Bro Code"

for char in name:
    if char == " ":
        continue  # skip spaces
    print(char, end=" ")  # print each character followed by a space

my_dictonary = {"A": 1, "B": 2, "C": 3}
# når man itererer over et dictonary returnerer det nøklene (keys) men ikke verdiene (values)

for value in my_dictonary.values():
    print(value, end=" ")  # print each value followed by a space 

for key, valie in my_dictonary.items():
    print(f"{key}: {valie}", end=" ")  # print each key-value pair followed by a space