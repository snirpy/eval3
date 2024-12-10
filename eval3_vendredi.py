# Réseau avec des trames simplifiées
reseau = {
    1: {"source": "192.168.0.1", "destination": "192.168.0.2", "type": "IPv4", "etat": "transmise"},
    2: {"source": "192.168.0.3", "destination": "192.168.0.4", "type": "ARP", "etat": "perdue"},
    3: {"source": "192.168.0.5", "destination": "192.168.0.6", "type": "IPv4", "etat": "transmise"},
}

# 1. Ajouter une trame
def ajouter_trame(id, source, destination, type, etat, reseau):
    if id in reseau:
        print(f"Erreur : L'ID {id} existe déjà.")
    else:
        reseau[id] = {"source": source, "destination": destination, "type": type, "etat": etat}
        print(f"Trame avec l'ID {id} ajoutée avec succès.")

# 2. Modifier l'état d'une trame
def modifier_etat_trame(id, nouvel_etat, reseau):
    if id not in reseau:
        print(f"Erreur : La trame avec l'ID {id} n'existe pas.")
    else:
        reseau[id]["etat"] = nouvel_etat
        print(f"L'état de la trame avec l'ID {id} a été modifié en '{nouvel_etat}'.")

# 3. Supprimer une trame
def supprimer_trame(id, reseau):
    if id not in reseau:
        print(f"Erreur : La trame avec l'ID {id} n'existe pas.")
    else:
        del reseau[id]
        print(f"Trame avec l'ID {id} supprimée.")

# 4. Afficher toutes les trames d'un type donné
def afficher_trames_par_type(type, reseau):
    trames_filtrees = [f"ID: {id}, Source: {trame['source']}, Destination: {trame['destination']}, Etat: {trame['etat']}"
                       for id, trame in reseau.items() if trame["type"] == type]
    if trames_filtrees:
        print(f"Trames de type {type} :")
        for trame in trames_filtrees:
            print(trame)
    else:
        print(f"Aucune trame de type {type} trouvée.")

# 5. Calculer les statistiques (trames perdues, etc.)
def calculer_statistiques(reseau):
    total_trames = len(reseau)
    trames_perdues = sum(1 for trame in reseau.values() if trame["etat"] == "perdue")
    pourcentage_perdues = (trames_perdues / total_trames) * 100 if total_trames > 0 else 0
    print(f"Statistiques :")
    print(f"Nombre total de trames : {total_trames}")
    print(f"Nombre de trames perdues : {trames_perdues}")
    print(f"Pourcentage de trames perdues : {pourcentage_perdues:.2f}%")

# Programme de test
ajouter_trame(4, "192.168.0.7", "192.168.0.8", "IPv4", "transmise", reseau)
ajouter_trame(5, "192.168.0.9", "192.168.0.10", "ARP", "perdue", reseau)
modifier_etat_trame(3, "perdue", reseau)
afficher_trames_par_type("IPv4", reseau)
calculer_statistiques(reseau)
supprimer_trame(2, reseau)
afficher_trames_par_type("ARP", reseau)
