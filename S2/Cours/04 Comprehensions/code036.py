squares_generator = ((x, x * x) for x in range(1_000_000))
print(squares_generator)

print(next(squares_generator))
(0, 0)
print(next(squares_generator))
(1, 1)
print(next(squares_generator))
(2, 4)
print(next(squares_generator))
(3, 9)