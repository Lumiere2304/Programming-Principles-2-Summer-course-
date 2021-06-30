# Exercise 1:
Elements = {"Pyro", "Hydro", "Electro", "Cryo", "Anemo", "Geo"}
if "Pyro" in Elements:
    print("Yes, Pyro is a Element!")

# Exercise 2:
Elements = {"Pyro", "Hydro", "Electro", "Cryo", "Anemo", "Geo"}
Elements.add("Dendro")
print(Elements)

# Exercise 3:
Elements = {"Ignis", "Aqua", "Aer", "Terra"}
Elements_New = {"Aether"}
Elements.update(Elements_New)
print(Elements)

# Exercise 4:
Elements = {"Ignis", "Aqua", "Aer", "Terra", "Aether"}
Elements.remove("Aether")
print(Elements)

# Exercise 5:
Elements = {"Ignis", "Aqua", "Aer", "Terra", "Aether"}
Elements.discard("Ignis")
print(Elements)

