from copy import deepcopy

def remove_employes(liste, *args):
    liste_temp = deepcopy(liste)
    for employe in args:
        while employe in liste_temp:
            liste_temp.remove(employe)
    return liste_temp

employes_origine = ["Patrick", "Julie", "Simon", "Paul", "Pauline"]


employes_final = remove_employes(employes_origine)
print(employes_final)
employes_final = remove_employes(employes_origine, "Patrick", "Paul")
print(employes_final)
print(employes_origine)