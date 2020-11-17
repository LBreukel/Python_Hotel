
# Made by: Luke Breukel
# Date: 30-10-2020

# Run this file!

import time
from inchecken import *
from uitchecken import*
from reserveren import *

gasten = []
bon = []

info = ["1 = Inchecken", "2 = Uitchecken", "3 = Restaurant", "4 = Exit"]

while True:
    print("Welkom in Motel a la Luke! Waar kan ik u mee helpen?")

    for i in info:
        print(i)

    keuze = input("Uw keuze: " )

    if keuze == '1':
        inchecken(gasten, bon)

    elif keuze == '2':
        uitchecken(gasten, bon)

    elif keuze == "3":
        reserveren(gasten, bon)

    elif keuze == '4':
        print("Geniet van uw verblijf en anders een fijne dag verder!")
        time.sleep(2)
        print(bon)
        break

    else:
        print("Dat is geen optie!")
        time.sleep(2)
        continue
