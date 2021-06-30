# Exercise 1:
car = {
    "company": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))

# Exercise 2:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2021
print(car.get("year"))

# Exercise 3:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car.get("color"))

# Exercise 4:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car.get("model"))

# Exercise 5:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car.get("company"))
