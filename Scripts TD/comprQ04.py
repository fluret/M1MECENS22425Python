liste_fruits = ["banane", "cerise", "kiwi", "orange", "pomme"]

remplace_voyelles = [''.join(['*' if car in 'aeiouy' else car for car in fruit]) for fruit in liste_fruits]