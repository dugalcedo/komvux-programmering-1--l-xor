# importera random så att jag kan använda random.randrange
import random

# en global variabel för spelarens rekord
rekord = 10

# en funktion för att börja (om) spelet
def spela():

    # jag skriver ut en tom rad så att det blir lite lättare att läsa
    print("")

    # jag vill kunna ändra den här globala variabeln
    global rekord

    # använder randrange för att generera ett nummer mellan 0 och 100
    slumptal = random.randrange(0, 100, 1)

    # en sträng som jag ska senare använda för att avgör spelets resultat
    resultat = ""

    # sätta antalet försök till 1
    gånger = 1

    # gissningen måste initieras för att whileloopen kan funka
    gissning = -1
    
    # skriv ut en välkommen meddelande
    print("Välkommen till gissaspelet!")
    
    # while loop som exekveras så länge som gissningen är fel och spelare har inte försökt mer än 10 gånger
    while slumptal != gissning and gånger < 11:
        print("")
        print("Ange ett nummer mellan 0 och 100 eller skriva 'ge upp' för att visa svaret.")
        # mäta in spelarens gissning
        gissning = input()

        """
        Om inmatningen är "ge upp"...
            Visa spelaren det korrekta svaret
            Fråga om hen vill försöka igen och anropa en funktion
            Avsluta "spela" funktionen
        """
        if gissning == "ge upp":
            print(f"Numret var {slumptal}.")
            print("Vill du försöka igen?  (ja/nej)")
            villDuSpelaIgen()
            return
        
        """
        Inmatningen är inte "ge upp", så konvertera det till heltal
        Om det är inte mellan 0 och 100, informera spelaren och upprepa whileloopen
        """
        gissning = int(gissning)
        if gissning > 100 or gissning < 0:
            print("Det var inte ett giltigt nummer.")
            continue

        # Om gissningen är korrekt, resultatet ska bli "vinn" och whileloopen ska avslutas
        if gissning == slumptal:
            resultat = "vinn"
            break
        
        """
        beräkna differensen mellan gisnningen och slumptalet
        räkna ut om det är hög eller låg och hur nära det är till det korrekta svaret
        utifrån detta, definiera några ord
        """
        diff = gissning - slumptal
        ord1 = "HÖG" if diff > 0 else "LÅG"
        ord2 = "inte" if abs(diff) > 20 else "något" if abs(diff) > 10 else "ganska" if abs(diff) > 5 else "väldigt"

        """
        Använda orden för att berätta för spelaren hur nära gissningen var.
        Öka antalet försök.
        Om det är över 10, resultatet ska bli "förlust".
        """
        print(f"Din gissning är för {ord1}. Du är {ord2} nära.")
        gånger += 1
        if gånger > 10:
            resultat = "förlust"
    # whileloopens avslutning

    # Nu som whileloopen har avslutats visar jag någon information till spelaren beroende på resultatet.
    if resultat == "vinn":
        """
        Om antalet försök är mindre en rekordet ska rekordet ersättas.
        Informera spelaren att de var korrekta och visa antalet försök och rekordet.
        Fråga om hen vill spela igen och anropa en funktion.
        """
        rekord = rekord if gånger > rekord else gånger
        print(f"Du har korrekt! Numret var {slumptal}.")
        print(f"Försök: {gånger}")
        print(f"Rekord: {rekord}")
        print("Vill du spela igen?  (ja/nej)")
        villDuSpelaIgen()
    elif resultat == "förlust":
        # Informera spelaren att de förlorade spelet. Visa korrekta svaret och fråga om hen vill spela igen.
        print(f"Du har inga försök kvar. Numret var {slumptal}. Vill du försöka igen? (ja/nej)")
        villDuSpelaIgen()

# Funktion som frågar spelaren om hen vill spela igen. Om jag, spela igen, annars hej då.
def villDuSpelaIgen():
    if input() == "ja":
        spela()
    else:
        print("Hej då!")

# Börja spelet för första gången
spela()