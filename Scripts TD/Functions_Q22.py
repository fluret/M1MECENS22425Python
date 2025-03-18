liste_val = [10, 20, 50, 120, 30, 65, 78, 26, 63, 74, 83]

def list_and_tuple(*nums):
    newlist = [str(num) for num in nums]
    newtuple = tuple(newlist)
    return newlist, newtuple

result1, result2 = list_and_tuple(*liste_val)

print("List:", result1)
print("Tuple:", result2)

