liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

tuple_final = (tuple((x, y, x+y) for x in liste1 for y in liste2 if (x+y) % 2 == 0),
               tuple((x, y , x+y) for x in liste1 for y in liste2 if (x+y) % 2 != 0))

print(tuple_final)