import random
import grafika

def tah_hrace(pole, slovo):
    while True:
        pokus = input("Zadej písmeno: ")
        if pokus.isalpha():
            break
    global vedle
    if pokus in slovo:
        pole = list(pole)
        pole[slovo.index(pokus)] = pokus
        pole = "".join(pole)
        return pole
    else:
        vedle += 1
        return pole

def vyhodnot(chyby):
    if "-" not in hraci_pole:
        print("Vyhrál jsi!")
        return 0
    if chyby > 0:
        print(grafika.staveni_sib[chyby])
    if chyby == 10:
        print(grafika.staveni_sib[-1])
        print("Prohrál jsi!")
        return 0

seznam_slov = ["python", "ladies", "kurz"]
hadane_slovo = random.choice(seznam_slov)

hraci_pole = len(hadane_slovo) * "-"
vedle = 0

print(hraci_pole)
while True:
    hraci_pole = tah_hrace(hraci_pole, hadane_slovo)
    if vyhodnot(vedle) == 0:
        print("Slovo:", hadane_slovo)
        break
    print("\n", hraci_pole)
