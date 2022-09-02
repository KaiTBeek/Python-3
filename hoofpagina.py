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
    print("1. Laat alle producten zijn")
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
    elif keuze == "3":
        print("Nu kan je een product verwijderen.")
        time.sleep(1)
        verwijdering = input("Welke product moet verwijderd worden? ")
        del producten[verwijdering]
    elif keuze == "4":
        print("Nu kun je het product of de prijs aanpassen. ")
        time.sleep(1)
        vraagievraagie = input("wil je de prijs of een product of beide aanpassen? ")
        if vraagievraagie == "Prijs":
            welke = input("Van welk product wil je de prijs aanpassen? ")
            if welke == "Brood":
                broodinput = input("Wat wordt de nieuwe prijs?")
                producten[2] = producten[broodinput]
                del producten[2]
            elif welke == "Water":
            elif welke == "Vlees":
            elif welke == "Groente":
            elif welke == "Fruit":
        else:
            welke = input("Welk product wil je aan passen?")

    elif keuze == "5":
        
while j < 6:
    menu()
    doorgaan = input("Wil je doorgaan? ")
    if doorgaan == "ja":
        j = j + 0
    elif doorgaan == "nee":
        j = j + 8
        print("Oke tot ziens!")