# funktion som konverterar fahrenheit till celsius
def fahrToCel(temp):
    return (temp - 32) * 5 / 9

try:
    print('Ange en temperatur på fahrenheit: ')
    # jag använder float() istället för int() i fallet användaren anger ett nummer med en decimalpunkt
    fahr = float(input())
    # jag anropar fahrToCel() men också round() för att runda siffran till max två decimal
    cel = round(fahrToCel(fahr), 2)
    print(f"{fahr}F = {cel}C")
except:
    # i fallet användaren inte anger ett nummer
    print("Det var inte en giltig temperatur")

