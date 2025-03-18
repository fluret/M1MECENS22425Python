points = {"poules": 1, "chiens: 3, "vaches": 5, "amis": 10}
          
def points_perdus(**kwargs):
    return sum(kwargs.get(victime, 0)* point for victime, point in points.items())

victimes ={}
victimes["poules"] = int(input("Combien de poules ? "))
victimes["chiens"] = int(input("Combien de chiens ? "))
victimes["vaches"] = int(input("Combien de vaches ? "))
victimes["amis"] = int(input("Combien d'amis ? "))
print(f"Vous avez perdu, {points_perdus(**victimes)}, points")

print(f'Vous devez payer {points_perdus(**victimes)*2} euros')
print(f'{Rien à payer if points_perdus(**victimes) == 0 else "Vous devez payer {points_perdus(**victimes)*2} euros"}')

