
# TODO: Graphisch darstellen

# Exponentielles Wachstum
def Wachstum(anzahlBakterien,p2):
    g0: int = anzahlBakterien# Anzahl an Bakterien
    p: float = p2 # p Prozent
    n: int = 0 # Tage


    while n < 10:
        n += 1
        p2: float = 1 + (7 / 100) # 1.07
        gn: float = g0 * p ** n
        gn = round(gn,2)
        print(f"{n}: {gn}")

Wachstum(100,15)

print()
# Exponentielle Abnahme
def Abnahme(anzahlBakterien2,p3):
    g0: int = anzahlBakterien2  # Startwert
    p: int = p3 # Prozentsatz der Abnahme
    tage: int = 10  # Anzahl der Tage
    
    p3 = 1 - p3 / 100 
    p3 = round(p3,2)


    for n in range(1, tage + 1):  # Für jeden Tag von 1 bis 10
        gn = g0 * p3 ** n  # Exponentielle Abnahme
        gn = round(gn, 2)  # Auf 2 Dezimalstellen runden
        print(f"{n}: {gn}")

Abnahme(100,15)



