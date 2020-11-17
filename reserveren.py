
#Made by: Luke Breukel
#Date: 02-11-2020

import time

optie = ["1 = Reserveren", "2 = Annuleren", "3 = Exit"]
type = ["1 = Ontbijt €10pp", "2 = Lunch €10pp", "3 = Diner €40pp" , "4 = Alles in 1 €100" ,"5 = Exit"]
type2 = ["1 = Ontbijt", "2 = Lunch", "3 = Diner" , "4 = Alles in 1"]
ontbijt = []
lunch = []
diner = []
alles = []

def reserveren(gasten, bon):
    while True:
        print("Waar kunnen we u met helpen?")

        for o in optie:
            print(o)
        keuze = input("Keuze: ")

        if keuze == "1":
            print("Welkom, wat wilt u reserveren?")

            for t in type:
                print(t)
            k = input("Keuze: ")

            if k == "1":
                while True:
                    naam = input("Onder welke naam verblijft u: ")
                    if naam in gasten:
                        print("De reservering voor het ontbijt is gemaakt!")
                        x = gasten.index(naam)
                        bon[x] = bon[x] + 10
                        ontbijt.append(naam)
                        time.sleep(2)
                        break
                    else:
                        print("U kan alleen reserveren als u een kamer heeft!")
                        break
            elif k == "2":
                while True:
                    naam = input("Onder welke naam verblijft u: ")
                    if naam in gasten:
                        print("De reservering voor de lunch is gemaakt!")
                        x = gasten.index(naam)
                        bon[x] = bon[x] + 10
                        lunch.append(naam)
                        time.sleep(2)
                        break
                    else:
                        print("U kan alleen reserveren als u een kamer heeft!")
                        break
            elif k == "3":
                while True:
                    naam = input("Onder welke naam verblijft u: ")
                    if naam in gasten:
                        print("De reservering voor het diner is gemaakt!")
                        x = gasten.index(naam)
                        bon[x] = bon[x] + 40
                        diner.append(naam)
                        time.sleep(2)
                        break
                    else:
                        print("U kan alleen reserveren als u een kamer heeft!")
                        break
            elif k == "4":
                while True:
                    naam = input("Onder welke naam verblijft u: ")
                    if naam in gasten:
                        print("De reserveringen zijn gemaakt!")
                        x = gasten.index(naam)
                        bon[x] = bon[x] + 100
                        alles.append(naam)
                        time.sleep(2)
                        break
                    else:
                        print("U kan alleen reserveren als u een kamer heeft!")
                        break
            elif k == "5":
                break
            else:
                print("Dat is geen optie")
                time.sleep(2)
                continue
        elif keuze == "2":
            while True:
                naam = input("Onder welke naam is er gereserveerd: ")
                if naam in gasten:
                    print("Wat wilt u annuleren?")

                    for a in type2:
                        print(a)
                    keuze = input("Keuze: ")

                    if keuze == "1":
                        if naam in ontbijt:
                            k = input("Weet u zeker dat u wilt annuleren (Ja/Nee): ")
                            k = k.lower()
                            if k == "ja":
                                print("De reservering is geannuleerd!")
                                x = gasten.index(naam)
                                bon[x] = bon[x] - 10
                                ontbijt.remove(naam)
                                time.sleep(2)
                                break
                            else:
                                break
                        else:
                            print("Er is geen reservering onder die naam!")
                            time.sleep(2)
                            continue

                    elif keuze =="2":
                        if naam in lunch:
                            k = input("Weet u zeker dat u wilt annuleren (Ja/Nee): ")
                            k = k.lower()
                            if k == "ja":
                                print("De reservering is geannuleerd!")
                                x = gasten.index(naam)
                                bon[x] = bon[x] - 10
                                lunch.remove(naam)
                                time.sleep(2)
                                break
                            else:
                                break
                        else:
                            print("Er is geen reservering onder die naam!")
                            time.sleep(2)
                            continue

                    elif keuze == "3":
                        if naam in diner:
                            k = input("Weet u zeker dat u wilt annuleren (Ja/Nee): ")
                            k = k.lower()
                            if k == "ja":
                                print("De reservering is geannuleerd!")
                                x = gasten.index(naam)
                                bon[x] = bon[x] - 40
                                diner.remove(naam)
                                time.sleep(2)
                                break
                            else:
                                break
                        else:
                            print("Er is geen reservering onder die naam!")
                            time.sleep(2)
                            continue
                    elif keuze == "4":
                        if naam in alles:
                            k = input("Weet u zeker dat u wilt annuleren (Ja/Nee): ")
                            k = k.lower()
                            if k == "ja":
                                print("De reservering is geannuleerd!")
                                x = gasten.index(naam)
                                bon[x] = bon[x] - 100
                                alles.remove(naam)
                                time.sleep(2)
                                break
                            else:
                                break
                        else:
                            print("Er is geen reservering onder die naam!")
                            time.sleep(2)
                            continue
                    else:
                        print("Dat is geen optie!")
                        time.sleep(2)
                        continue
                else:
                    print(naam, "is geen gast van dit hotel!")
                    continue

        elif keuze == "3":
            break
        else:
            print("Dat is geen optie!")
            time.sleep(2)
            continue
