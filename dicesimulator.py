#===============================================
#              WÜRFELSIMULATOR 3000
#===============================================

from random import randint

def ist_int(zahl):
    try:
        int(zahl)
        return True
    except ValueError:
        return False
    
def wuerfeln(n):
    for i in range(n):
        wurf = randint(1, 6)
        liste.append(wurf)

    mean = sum(liste) / n
    
    print("Berechneter Mittelwert:", mean)
    print("Theoretischer Mittelwert: 3,5")
    return 



while True:

    n = input("Wie oft soll gewürfelt werden? Bitte gebe eine ganze Zahl ein.")
    if ist_int(n):
        n = int(n)
    else:
        print("Deine Eingabe ist ungültig. Sie muss eine ganze zahl sein. Wiederhole dein Eingabe:")
        continue


    liste = []

    wuerfeln(n)

    exit = input("Möchtest du noch was ausrechnen? j / n")
    if exit == "n":
            break
    elif exit == "j":
            continue
    else:
         break






