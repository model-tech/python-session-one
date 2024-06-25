def afficher_table_multiplication():
    try:
        chiffre = int(input("Entrez un chiffre entre 2 et 9 : "))
        if 2 <= chiffre <= 9:
            print(f"Table de multiplication pour {chiffre} :")
            for i in range(1, 13):
                resultat = chiffre * i
                print(f"{chiffre} x {i} = {resultat}")
        else:
            print("Le chiffre doit être entre 2 et 9.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
