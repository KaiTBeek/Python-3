# print menu
# als keuze == 1
#   dan laat alle producten zien
# als keuze == 2
#   dan voeg een product toe
# als keuze == 3
#     dan verwijder een product
# als keuze == 4
#     dan product of prijs wijziging
# als keuze == 5
#     dan boodschappen doen + totale prijs

import time
j = 1
producten = {"Brood": 2, "Water": 1, "Vlees": 1.50, "Groente": 4, "Fruit": 2.50}
print("Hallo en welkom. Hier kunt u uw boodschappen doen.")
time.sleep(3)
print("Je kan kiezen tussen 5 verschillende keuzes.")
time.sleep(3)
def menu():
    kosten = 0
    print("1. Laat alle producten zien")
    time.sleep(1)
    print("2. Producten toevoegen")
    time.sleep(1)
    print("3. Producten Verwijderen")
    time.sleep(1)
    print("4. Product of prijs aanpassen")
    time.sleep(1)
    print("5. De boodschappen doen")
    time.sleep(1)
def inputverwerk():
    keuze = input("Welk van deze vijf keuzes wil je? ")
    if keuze == "1":
        print(producten)
    elif keuze == "2":  
        print("Nu kan je een product toevoegen.")
        time.sleep(1)
        toevoeging = input("Welke product wil je toevoegen? ")
        toevoeging1 = float(input("Hoeveel kost het product? "))
        producten[toevoeging] = toevoeging1
        print(producten)
    elif keuze == "3":
        print("Nu kan je een product verwijderen.")
        time.sleep(1)
        print(producten)
        verwijdering = input("Welk van deze producten moet verwijderd worden? ")
        del producten[verwijdering]
        time.sleep(1)
        print("Nu zit de lijst er zo uit!")
        print(producten)
    elif keuze == "4":
        print("Nu kun je het product of de prijs aanpassen. ")
        time.sleep(1)
        vraagievraagie = input("wil je de prijs of een product of beide aanpassen? ")
        if vraagievraagie == "Prijs" or vraagievraagie == "prijs":
            print(producten)
            welke = input("Van welk product wil je de prijs aanpassen? ")
            if welke == "Brood" or welke == "brood":
                broodinput = float(input("Wat wordt de nieuwe prijs? "))
                producten["Brood"] = broodinput
            elif welke == "Water" or welke == "water":
                waterinput1 = float(input("Wat wordt de nieuwe prijs? "))
                producten["Water"] = waterinput1
            elif welke == "Vlees" or welke == "vlees":
                vleesinput2 = float(input("Wat wordt de nieuwe prijs? van vlees "))
                producten[welke] = vleesinput2
            elif welke == "Groente" or welke == "groente":
                groenteinput3 = float(input("Wat wordt de nieuwe prijs? "))
                producten["Groente"] = groenteinput3
            elif welke == "Fruit" or welke == "fruit":
                fruitinput4 = float(input("Wat wordt de nieuwe prijs? "))
                producten["Fruit"] = fruitinput4
        else:
            welke1 = input("Welk product wil je aan passen? ")
            if welke1 == "Brood" or welke1 == "brood":
                productbrood = input("Wat is het nieuwe product? ")
                producten[productbrood] = producten["Brood"]                    
                del producten["Brood"]
                prijs = float(input("Wat wordt de prijs van dit product? "))
                producten[productbrood] = prijs
                print(producten)
            elif welke1 == "Water" or welke1 == "water":
                productwater = input("Wat is het nieuwe product? ")
                producten[productbrood] = producten["Water"]                    
                del producten["Water"]
                prijs = float(input("Wat wordt de prijs van dit product? "))
                producten[productwater] = prijs
                print(producten)
            elif welke1 == "Vlees" or welke1 == "vlees":
                productvlees = input("Wat is het nieuwe product? ")
                producten[productvlees] = producten["Vlees"]                    
                del producten["Vlees"]
                prijs = float(input("Wat wordt de prijs van dit product? "))
                producten[productvlees] = prijs
                print(producten)
            elif welke1 == "Groente" or welke1 == "groente":
                productgroente = input("Wat is het nieuwe product? ")
                producten[productgroente] = producten["Groente"]                    
                del producten["Groente"]
                prijs = float(input("Wat wordt de prijs van dit product? "))
                producten[productgroente] = prijs
                print(producten)
            elif welke1 == "Fruit" or welke1 =="fruit":
                productfruit = input("Wat is het nieuwe product? ")
                producten[productfruit] = producten["Fruit"]                    
                del producten["Fruit"]
                prijs = float(input("Wat wordt de prijs van dit product? "))
                producten[productfruit] = prijs
                print(producten)
            else:
                print("Dat product staat niet in de lijst!")
    elif keuze == "5":
        time.sleep(1)
        print("Hier kan u uw boodschappen doen! ")
        time.sleep(1)
        print(producten)
        for x in producten:
            time.sleep(1)
            boodschappen = input("Welke producten wil je toevoegen aan je lijst? (zeg 'stop' als je kaar bent) ")
            if boodschappen == "stop" or boodschappen == "Stop":
                print("dat wordt dan " + str(kosten) + " euro!")
                time.sleep(1)
                print("Dank voor uw boodschappen!")
                time.sleep(1)
                break
                kosten += producten[boodschappen]

while j < 6:
    menu()
    inputverwerk()
    doorgaan = input("Wil je doorgaan? (als je stopt blijft er niks opgeslagen) ")
    if doorgaan == "ja":
        j = j + 0
    elif doorgaan == "nee":
        j = j + 8
        print("Oke tot ziens!")