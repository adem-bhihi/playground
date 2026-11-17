import sys

if len(sys.argv)>2:
    nom=sys.argv[1]
    age=sys.argv[2]
    try:
        print(f"salut {nom}, tu as {age}. Dans 10 ans tu auras {int(age)+10}ans.")
    except ValueError:
        print("L'âge doit être un nombre")
else:
    print("Utilisation : python greet.py <prénom> <âge>")
