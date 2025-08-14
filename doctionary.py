# dictionary =  a collection of {key:value} pairs
#               ordered and changeable. No duplicates


capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "D.C."})  # This will not change the value since it's the same
capitals.pop("China")  # Removes the key-value pair for China
capitals.popitem()  # Removes the last inserted key-value pair
capitals.clear()  # Clears the dictionary

keys = capitals.keys()  # Returns a view object displaying a list of all the keys
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()  # Returns a view object displaying a list of all the values
print(values) #returnerer ett object som kan itereres gjennom

for value in capitals.values():
    print(value)

items = capitals.items()  # Returns a view object displaying a list of key-value pairs
print(items) #returnerer en 2d liste av tuple med key og value
for key, value in capitals.items():
    print(f"{key}: {value}")

print(capitals)