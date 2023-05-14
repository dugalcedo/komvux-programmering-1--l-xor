"""
    importera random
    definiera bingo bokstav
    definiera en vektor för att hålla koll på utvalda bollar
"""

import random
bingo = "BINGO"
utvaldaBollar = []

# funktion för att skapa spelarens bingo bricka
def skapaBricka():
    bricka = []
    # den här loopen skapar en tvådimensionell array där varje inre array representerar en rad på brickan
    # varje rad har fem rutor med slumptal mellan 0 och 9
    for i in range(0, 5):
        rad = []
        for j in range(0, 5):
            rad.append(random.randint(0, 9))
        bricka.append(rad)
    # den centrala rutan är en "free space"
    bricka[2][2] = "F"
    return bricka

# funktion för att skapa ett "spelläge" vilket är en 2D array som håller koll på vilka rutor är "träffade"
# True betyder träffat
def spelLäge():
    läge = []
    for i in range(0,5):
        rad = []
        for j in range(0, 5):
            rad.append(False)
        läge.append(rad)
    # den centrala rutan är gratis
    läge[2][2] = True
    return läge

# funktion för att kontrollera spelläget och print "BINGO" om spelare vinner
# return True om spelet har vunnits
def kontrollera(läge):
    # kontrollera för horisontell bingo
    for rad in läge:
        if all(rad): return True
    # kontrollera för vertikal bingo
    for n in range(0, 5):
        if all([läge[0][n],läge[1][n],läge[2][n],läge[3][n],läge[4][n]]): return True
    # kontrollera för diagonal bingo, topp-vänster till botten-höger
    if all([läge[0][0],läge[1][1],läge[2][2],läge[3][3],läge[4][4]]): return True
    # kontrollera för diagonal bingo, botten-vänster till topp-höger
    if all([läge[0][4],läge[1][3],läge[2][2],läge[3][1],läge[4][0]]): return True

# spelets huvudfunktion
def spela():
    print("Välkommen till Bingo! Varsågod ta din bricka!")
    # utvaldaBollar är global
    global utvaldaBollar
    # varje spel bör det återställs tomt
    utvaldaBollar = []
    # hämta brickan och läget
    bricka = skapaBricka()
    läge = spelLäge()

    # spelloopen avslutas när bollarna tar slut (50 total) eller spelLäget() returner True
    while(len(utvaldaBollar) <= 50):
        boll = skaffaBoll()
        # den här lilla loopen ser till att vi inte får uprepande bollar
        while boll in utvaldaBollar: boll = skaffaBoll()
        # lägga bollen till utvaldaBollar
        utvaldaBollar.append(boll)
        print(f"Bollen är {boll}")
        visaBricka(bricka, läge)
        # om kontrollera return True, spelet har vunnits
        if kontrollera(läge): 
            print("BINGO! Du vann.")
            break
        print("Tryck enter/return för nästa bollen.")
        input()
    print("Spela igen? (ja/nej)")
    if input() == "ja":
        spela()
    else:
        print("Hej då!")
    
def visaBricka(bricka, läge):
    # skriv ut översta raden
    print("  B  |  I  |  N  |  G  |  O  ")
    linje()
    # jag använder enumerate() så att jag får tillgång till indexen i arrayerna
    for index1, rad in enumerate(bricka):
        # brikaRad ska innehålla strängar för det "tryckbara" brickan
        brickaRad = []
        for index2, n in enumerate(rad):
            # jag kan använda index2 för att hämta det bingobokstav jag behöver
            boll = f"{bingo[index2]}{n}"
            # om bollen finns i utvaldaBollar betyder det att det ska omges av parentes
            # parenteserna ska representera en träffad ruta
            if boll in utvaldaBollar:
                ruta = f" ({n}) "
                # jag kombinerar index1 och index2 för att markera den respektiva booleanen i spelläget
                läge[index1][index2] = True
            else: 
                ruta = f"  {n}  "
            # den gratis rutan ska alltid vara markerad
            if n == "F": ruta = " (F) "
            brickaRad.append(ruta)
        # skriv ut raden
        print(f"{brickaRad[0]}|{brickaRad[1]}|{brickaRad[2]}|{brickaRad[3]}|{brickaRad[4]}")
        linje()

# funktion för att skaffa en slumpboll
def skaffaBoll():
    bokstav = bingo[random.randint(0, 4)]
    n = random.randint(0, 9)
    boll = f"{bokstav}{n}"
    return boll
        
# funktion för att skaffa en skjilande linje på den tryckbara brickan
def linje():
    print("-----------------------------")

# börjar spelet för första gången
spela()