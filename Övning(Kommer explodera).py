import random

korrekt = False

hemligtnummer = random.randint(1, 2)

while korrekt == False:
    nummergissning = int(input("Skriv ett nummer: "))
    if nummergissning == hemligtnummer:
        print("Du hade rätt!")
        korrekt = True
    else:
        print("Fel.")

