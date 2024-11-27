import matplotlib.pyplot as plt
import numpy as np



def Wachstum(anzahlBakterien,p2,tage):
     standardBeispielWert: int = 1
     g0: int = anzahlBakterien # Anzahl an Bakterien
     p2: float = 1 + (p2 / 100)
     p = p2
     days = np.arange(1,tage)
     countBacteria = []

     print(f"Bakt: {g0} q: {p} ")


     for n in days:
         gn: float = g0 * p ** n
         gn = round(gn,2)
         countBacteria.append(gn)

         print(f"{n}: {gn}")

     print(f"{gn},{g0},{p},{n}")
        
     plt.figure(figsize=(8, 5)) # Größe des Bildes
     plt.plot(days, countBacteria, marker='', label='Bakterien Wachstum')
     plt.title('Exponentieller Wachstum')
     plt.xlabel('Days')
     max_bacteria = max(countBacteria) # maximale Anzahl and Bakterien
     yticks = np.arange(0, max_bacteria ,150) # 0 - max_bacteria in 150iger steps
     plt.yticks(yticks)

     plt.ylabel('Anzahl von Bakterien')
     plt.grid(True)
     #plt.legend()
     plt.show()

        

Wachstum(1,15,50)
