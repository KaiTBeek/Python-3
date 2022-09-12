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
producten = {"Brood": "2", "Water": "1", "Vlees": "10", "Groente": "4", "Fruit": "2,50"}
def menu():
    print("Hallo en welkom. Hier kunt u uw boodschappen doen.")
    time.sleep(3)
    print("Je kan kiezen tussen 5 verschillende dingen.")
    time.sleep(3)
    print("1. Laat alle producten zien")
    time.sleep(2)
    print("2. Producten toevoegen")
    time.sleep(2)
    print("3. Producten Verwijderen")
    time.sleep(2)
    print("4. Product of prijs aanpassen")
    time.sleep(2)
    print("5. De boodschappen doen")
    time.sleep(2)
    keuze = input("Welke van deze vijf keuzes wil je? ")
    if keuze == "1":
        print(producten)
    elif keuze == "2":  
        print("Nu kan je een product toevoegen.")
        time.sleep(1)
        toevoeging = input("Welke product wil je toevoegen? ")
        toevoeging1 = input("Hoeveel kost het product? ")
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
                broodinput = input("Wat wordt de nieuwe prijs? ")
                producten["Brood"] = broodinput
            elif welke == "Water" or welke == "water":
                waterinput1 = input("Wat wordt de nieuwe prijs? ")
                producten["Water"] = waterinput1
            elif welke == "Vlees" or welke == "vlees":
                vleesinput2 = input("Wat wordt de nieuwe prijs? van vlees ")
                producten[welke] = vleesinput2
            elif welke == "Groente" or welke == "groente":
                groenteinput3 = input("Wat wordt de nieuwe prijs? ")
                producten["Groente"] = groenteinput3
            elif welke == "Fruit" or welke == "fruit":
                fruitinput4 = input("Wat wordt de nieuwe prijs? ")
                producten["Fruit"] = fruitinput4
        else:
            welke1 = input("Welk product wil je aan passen? ")
            if welke1 == "Brood" or welke1 == "brood":
                productbrood = input("Wat is het nieuwe product? ")
                producten[productbrood] = producten["Brood"]                    
                del producten["Brood"]
                prijs = input("Wat wordt de prijs van dit product? ")
                producten[productbrood] = prijs
                print(producten)
            elif welke1 == "Water" or welke1 == "water":
                productwater = input("Wat is het nieuwe product? ")
                producten[productbrood] = producten["Water"]                    
                del producten["Water"]
                prijs = input("Wat wordt de prijs van dit product? ")
                producten[productwater] = prijs
                print(producten)
            elif welke1 == "Vlees" or welke1 == "vlees":
                productvlees = input("Wat is het nieuwe product? ")
                producten[productvlees] = producten["Vlees"]                    
                del producten["Vlees"]
                prijs = input("Wat wordt de prijs van dit product? ")
                producten[productvlees] = prijs
                print(producten)
            elif welke1 == "Groente" or welke1 == "groente":
                productgroente = input("Wat is het nieuwe product? ")
                producten[productgroente] = producten["Groente"]                    
                del producten["Groente"]
                prijs = input("Wat wordt de prijs van dit product? ")
                producten[productgroente] = prijs
                print(producten)
            else:
                productfruit = input("Wat is het nieuwe product? ")
                producten[productfruit] = producten["Fruit"]                    
                del producten["Fruit"]
                prijs = input("Wat wordt de prijs van dit product? ")
                producten[productfruit] = prijs
                print(producten)
while j < 6:
    menu()
    doorgaan = input("Wil je doorgaan? ")
    if doorgaan == "ja":
        j = j + 0
    elif doorgaan == "nee":
        j = j + 8
        print("Oke tot ziens!")