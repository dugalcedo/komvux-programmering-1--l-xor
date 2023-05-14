import random

# funktion för att konvertera fahrenheit till celsius
def fahrToCel(temp):
    return (temp - 32) * 5 / 9

# funktion för att returera ett slumptal
def slumpa():
    return random.randint(1, 200)

# initiera en temperatur som ska avsluta loopen när det blir lagom
temp = 0

# loopen ska avslutas när temp är mellan (inklusive) 82 och 87
while (temp < 82 or temp > 87):
    try:
        # be användaren att tillföra ett heltal
        print("Ange en temperatur på fahrenheit (heltal): ")
        # konvertera inmatningen till heltal
        fahr = int(input())
        # om 0 tillförs, anropa den slumptal metoden
        if fahr == 0:
            fahr = slumpa()
        # tilldela det konverterade numret till variabeln "temp"
        # runda så att det inte blir en massa siffror
        temp = round(fahrToCel(fahr), 1)

        # visa användaren den konverterade temperaturen
        print(f"Tempuraturen är {temp}C.")

        # visa olika meddelande beronde på om det är för kallt, för varmt, eller lagom
        if temp < 82:
            print("Det är för kallt.")
        elif temp > 87:
            print("Det är för varmt.")
        else:
            print("Temperaturen är bra. Bastun är nu redo att bada i.")
    #om användaren anger något som är inte ett heltal
    except:
        print("Det var inte ett heltal")