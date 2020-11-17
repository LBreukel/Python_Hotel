
# Made by: Luke Breukel
# Date: 30-10-2020

import time

type = ["1 = Normaal (2p) €50", "2 = Familie (4p) €80", "3 = Exit"]
kamers = [5, 10]
prijs = [50, 80]
gNormaal = []
gFamilie = []

def inchecken(gasten, bon):
    while True:
        print("Wat voor type kamer wilt u: ")
        for t in type:
            print(t)
        keuze = input("Type: ")

        if keuze == "1":
            aantalN = kamers[0] - len(gNormaal)
            if aantalN > 0:
                print("Er zijn nog", aantalN ,"kamers beschikbaar!")
                ant = input("Bevestigen Ja/Nee: " )
                ant = ant.lower()
                if ant == "ja":
                    while True:
                        naam = input("Op welke naam mag de kamer: ")
                        if naam not in gasten:
                            nachten = int(input("Hoeveel nachten: "))
                            totaal = 50 * nachten
                            gNormaal.append(naam)
                            gasten.append(naam)
                            bon.append(totaal)
                            print("Inchecken gelukt onder de naam:", naam)
                            time.sleep(2)
                            break
                        else:
                            print("Sorry die naam bestaat al!")
                            time.sleep(2)
                            continue
                    break
                elif ant == "nee":
                    continue
                else:
                    print("Dat is geen optie!")
                    time.sleep(2)
                    continue
            elif aantalN <= 0:
                print("Jammer genoeg zijn er geen kamers meer :(")
                continue
            else:
                continue
        elif keuze == "2":
            aantalF = kamers[1] - len(gFamilie)
            if aantalF > 0:
                print("Er zijn nog", aantalF,"kamers beschikbaar!")
                ant = input("Bevestigen Ja/Nee: ")
                ant = ant.lower()
                if ant == "ja":
                    while True:
                        naam = input("Op welke naam mag de kamer: ")
                        if naam not in gasten:
                            nachten = int(input("Hoeveel nachten: "))
                            totaal =80 * nachten
                            gFamilie.append(naam)
                            gasten.append(naam)
                            bon.append(totaal)
                            print("Inchecken is gelukt onder de naam: ", naam)
                            time.sleep(2)
                            break
                        else:
                            print("Sorry die naam bestaat al!")
                            time.sleep(2)
                            continue
                    break
                elif ant == "nee":
                    continue
                else:
                    print("Dat is geen optie!")
                    time.sleep(2)
                    continue
            elif aantalF <= 0:
                print("Jammer genoeg zijn er geen kamers meer :(")
                continue
        elif keuze == "3":
            break
        else:
            continue
