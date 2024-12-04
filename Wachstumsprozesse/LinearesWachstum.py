import random

def LinearesWachstum(faktor: int,startwert: float,maxSchritte: int):
    aktuelleSchritte = -1
    while aktuelleSchritte < maxSchritte:
        aktuelleSchritte += 1
        result = startwert + faktor * aktuelleSchritte

        print(f"Ergebniss[{aktuelleSchritte}]: {result}")


LinearesWachstum(random.randint(2,20),random.randint(2,500),10)
