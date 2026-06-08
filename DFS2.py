from map import *

pocet_radku = len(mapa_2)
pocet_sloupcu = len(mapa_2[0])

for y in range(pocet_radku): 
    for x in range(pocet_sloupcu):
        aktualni_znak = mapa_2[y][x]
        if aktualni_znak == 'S': 
            start_x = x 
            start_y = y

zasobnik = [(start_y, start_x)]
navstiveno = [(start_y, start_x)]
rodice = {}
cil_nalezen = False 

while len(zasobnik) > 0: 
    aktualni_y, aktualni_x = zasobnik.pop()
    if mapa_2[aktualni_y][aktualni_x] == 'K': 
        print("Mám cíl")
        cil_nalezen = True
        break 
    smery = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for zmena_y, zmena_x in smery: 
        novy_y = aktualni_y + zmena_y
        novy_x = aktualni_x + zmena_x

        if (0 <= novy_y < pocet_radku) and (0 <= novy_x < pocet_sloupcu) and (mapa_2[novy_y][novy_x] != '#') and ((novy_y, novy_x) not in navstiveno):
            zasobnik.append((novy_y, novy_x))
            navstiveno.append((novy_y, novy_x))

            rodice[(novy_y, novy_x)] = (aktualni_y, aktualni_x)
print(f"Počet cest, kudy jsem zkoušel jít {len(navstiveno)}")
if cil_nalezen: 
    cesta = []
    aktualni_bod = (aktualni_y, aktualni_x)

    while aktualni_bod != (start_y, start_x): 
        cesta.append(aktualni_bod)
        aktualni_bod = rodice[aktualni_bod]

    cesta.append((start_y, start_x))
    cesta.reverse()
    print(f"Tady je cesta {cesta}")
else: 
    print("Cíl nebyl nalezen :(")