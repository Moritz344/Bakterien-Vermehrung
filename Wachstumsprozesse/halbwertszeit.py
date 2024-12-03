import random

def halbwertszeit(endwert:int,wert:int,):
    faktor: float = 0.5
    zeit: int = -1
    while zeit < endwert:
        zeit += 1
        result = wert * faktor ** zeit
        print(f"Halbwertszeit:[{zeit}]",result)
    

halbwertszeit(10,random.randint(0,1000))

