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
print(capitals)