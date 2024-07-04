def mention_note(note):
    if note >= 18:
        return "Excellent"
    elif note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Satisfaisant"
    elif note >= 10:
        return "Passable"
    else:
        return "Échec"

# Demander à l'utilisateur d'entrer une note (en utilisant la gestion d'erreur pour s'assurer que l'entrée est numérique)
while True:
    try:
        note = float(input("Entrez votre note : "))
        break
    except ValueError:
        print("Veuillez entrer une valeur numérique.")

# Afficher la mention obtenue en appelant la fonction mention_note
mention = mention_note(note)
print(f"Votre mention est : {mention}")


 