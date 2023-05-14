"""
Hjälpkod för att komma igång
 * Notera att båda klasserna är i samma fil för att det ska underlätta.
 * Om programmet blir större bör man ha klasserna i separata filer såsom jag går genom i filmen
 * Då kan det vara läge att ställa in startvärden som jag gjort.
 * Man kan också skriva ut saker i konsollen i konstruktorn för att se att den "vaknar"
 * Denna kod hjälper mest om du siktar mot betyget E och C
 * För högre betyg krävs mer självständigt arbete
"""
from buss import Buss

class Program:
    def __init__(self, *args):
        # Skapar ett objekt av klassen Buss som heter minbuss
        # Denna del av koden kan upplevas väldigt förvirrande. 
	# Men i sådana fall är det bara att "skriva av".
        minbuss = Buss()
        minbuss.run()

        # "press any key to continue" blir lite svårt i python. För att göra detta behövs antingen 
        # en specialgjord funktion eller en "Python module" som hanterar tangenttryck
        # Den enklaste lösningen har jag skrivit nedan, att trycka på enter för att komma vidare
        # input("Press Enter to continue . . . ")

# Nedanstående kod är kryptisk. Om ni vill kan ni behålla de raderna.
# Följande kod aktiveras när denna python fil körs
if __name__ == "__main__":
    # skapa en instans (kopia) av klassen Program 
    my_program = Program()
