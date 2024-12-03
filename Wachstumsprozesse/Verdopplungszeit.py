import random

def verdopplungszeit(endwert:int,wert: int):
    faktor : int = 2
    zeit: int = 0
    while zeit < endwert:
        zeit += 1
        result = wert * faktor**zeit
        print(f"Ergebnis:[{zeit}]",result)


verdopplungszeit(10,random.randint(0,100))


