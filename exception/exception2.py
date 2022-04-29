def dire_bonjour_a (nom): 
    if nom=='': 
        raise ValueError("la fonction n'accepte pas de chaine vide")
   
    if type(nom)!= str: 
            raise ValueError("le nom doit etre de type str ")

    print("Bonjour",nom)


try: 
    dire_bonjour_a('maha')
except ValueError as exc: 
    print("erreur, message ", exec)