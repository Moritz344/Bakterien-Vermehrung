import math
def log(faktor: float,number: float):
    a = math.log10(number)
    b = math.log10(faktor)

    result = a / b
    print(result)

log(5,25)

