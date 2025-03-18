def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)
squared = map(lambda x: x ** 2, numbers)
print(list(squared))
print(list(squared))