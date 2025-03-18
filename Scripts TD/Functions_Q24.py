comptes = {
    "compte1": {"nom": "Dupont", "prenom": "Jean", "epargne": 1000},
    "compte2": {"nom": "Martin", "prenom": "Marie", "epargne": 0},
    "compte3": {"nom": "Durand", "prenom": "Pierre", "epargne": 1500},
    "compte4": {"nom": "Dupont", "prenom": "Sophie", "epargne": 3000},
    "compte5": {"nom": "Bernard", "prenom": "Luc", "epargne": 2500},
    "compte6": {"nom": "Martin", "prenom": "Claire", "epargne": -200},
    "compte7": {"nom": "Dupont", "prenom": "Julien", "epargne": 4000},
    "compte8": {"nom": "Garnier", "prenom": "Alice", "epargne": 3500},
    "compte9": {"nom": "Martin", "prenom": "Thomas", "epargne": -1500}
}

def synthesefamilles(**kwargs):
    synthese={}
    for compte in kwargs.values():
        if compte["nom"] not in synthese:
            synthese[compte["nom"]] = compte.get("epargne",0)
        else:
            synthese[compte["nom"]] += compte["epargne"]
    pauvre = min (synthese, key=synthese.get)
    riche = max (synthese, key=synthese.get)
    return (pauvre, synthese[pauvre], riche, synthese[riche])

print(synthesefamilles(**comptes))