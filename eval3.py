reseau = {
    101: {"nom": "Capteur de température", "etat": "inactif"},
    102: {"nom": "Capteur d'humidité", "etat": "actif"},
    103: {"nom": "Capteur de pression", "etat": "inactif"}
}

def ajouter_peripherique(id, nom, etat, reseau):
    if id in reseau:
        print(f"L'id: {id} existe déjà")
    else:
        reseau[id] = {"nom": nom, "etat": etat}
        print(f"Élément avec l'id: {id} a été ajouté avec succès")


# Programme de test
ajouter_peripherique(104, "Capteur de luminosité", "actif", reseau)
















def supprimer_peripherique(id, reseau):
    if id not in reseau:
        print(f"Le périphérique avec l'id: {id} n'existe pas.")
    else:
        del reseau[id]
        print(f"Le périphérique avec l'id: {id} a été supprimé.")

def modifier_etat(id, etat, reseau):
    if id not in reseau:
        print("Modification impossible. L'id n'existe pas.")
    else:
        reseau[id]["etat"] = etat
        print(f"L'état du périphérique avec l'id: {id} a été modifié en '{etat}'.")

def afficher_peripheriques_actifs(reseau):
    actifs = [f"{id}: {infos['nom']} (État: {infos['etat']})" for id, infos in reseau.items() if infos["etat"] == "actif"]
    if actifs:
        print("Périphériques actifs :")
        for actif in actifs:
            print(actif)
    else:
        print("Aucun périphérique actif.")

# Programme de test
ajouter_peripherique(104, "Capteur de luminosité", "actif", reseau)
# modifier_etat(103, "actif", reseau)
# afficher_peripheriques_actifs(reseau)
# supprimer_peripherique(102, reseau)
# afficher_peripheriques_actifs(reseau)
