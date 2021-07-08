# Exercise 1:
x = lambda a, b, c : (a + b) *c
print(x(5, 3, 3))

# Additional Exercise:
def my_function(n):
    return lambda a, b : (a * b) // n
myseparator = my_function(2)
print(myseparator(5, 8))