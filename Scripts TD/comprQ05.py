mot1 = "Camion"
mot2 = "Voiture"

lettre_en_commun = tuple(char for char in mot1 if char in mot2)

print("Les lettres en commun entre", mot1, "et", mot2, "sont :", lettre_en_commun)
