
# Made by: Luke Breukel
# Date: 30-10-2020

import time

def uitchecken(gasten, bon):

    while True:
        keuze = input("Wilt u uitchecken? Ja/Nee: ")
        keuze = keuze.lower()

        if keuze == "ja":
            naam = input("Onder welke naam heeft u een kamer?: ")

            if naam in gasten:
                x = gasten.index(naam)
                totaal = bon[x]
                print("U moet nog: €",totaal," betalen")

                time.sleep(1)

                keuze = input("Afreken? Ja/Nee: ")
                keuze = keuze.lower()
                if keuze == "ja":
                    gasten.remove(naam)
                    del bon[x]
                    print("Betaald!")
                    time.sleep(2)
                    break
                elif keuze == "nee":
                    continue
                else:
                    print("Dat is geen optie!")
                    time.sleep(2)
                    continue
            else:
                print(naam, "staat niet in het systeem!")
                continue
        elif keuze == "nee":
            break
        else:
            print("Dat is geen optie!")
            continue
