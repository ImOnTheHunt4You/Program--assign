import random
goob = True
burp = 0
print("Föreställ dig att du är i ett casino och kan vinna extrema summor med pengar, och detta är spelets regler:")
print("Målet är att komma så nära 21 som möjligt, du kommer slå en D6 och för varje slag får du avgöra om du vill slå igen eller  inte.")
print("Slår du över 21 så förlorar du alla dina besparingar, vinner du så dubblar du alla dina pengar.")
while goob == True:
    gambling = int(input("Type '1' for roll. Type '2' to stop playing. "))
    if gambling == 1:
        roll = random.randint(1,6)
        print("The dice rolled", roll)
        burp = burp + roll
        if burp > 21: 
            print("You lost everything.")
            break
        elif burp == 21:
            print("You doubled your savings.")
        else:
            print(burp)
    elif gambling == 2: 
        print("You have decided to stop playing, your score is", burp , "/ 21")
        break
    else:
        print("You went over 21.")

