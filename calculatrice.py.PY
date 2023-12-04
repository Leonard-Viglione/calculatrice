def addition(nombre1, nombre2):
    return nombre1 + nombre2

def soustraction(nombre1, nombre2):
    return nombre1 - nombre2

def multiplication(nombre1, nombre2):
    return nombre1 * nombre2

def division(nombre1, nombre2):
    if nombre2 != 0:
        return nombre1 / nombre2
    else:
        raise ValueError("Erreur : division par zéro")

def calculatrice():
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))
        operateur = input("Entrez l'opération (+, -, *, /) : ")

        if operateur == '+':
            resultat = addition(nombre1, nombre2)
        elif operateur == '-':
            resultat = soustraction(nombre1, nombre2)
        elif operateur == '*':
            resultat = multiplication(nombre1, nombre2)
        elif operateur == '/':
            resultat = division(nombre1, nombre2)
        else:
            raise ValueError("Erreur : opération non valide")

        print(f"Le résultat de {nombre1} {operateur} {nombre2} est : {resultat}")

    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

# Appel de la fonction principale
calculatrice()