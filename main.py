#Konwerter jednostki temperatury
celcius = float(input("Podaj temperaturę w °C: "))

farenheit = 32 + (1.8 * celcius)
kelvin = celcius + 273.15
reaumur = celcius * 0.8

print("Co chcesz abym wykonał?")
print("1. Zamień na stopnie Fahrenheita.")
print("2. Zamień na Kelwiny.")
print("3. Zamień na stopnie Réaumura.")
print("4. Wyświetl wszystko!")
choice = int(input("Wybieram: "))

if (choice==1):
    print(celcius, "°C =", farenheit, "°F")
elif (choice==2):
    print(celcius, "°C =", kelvin, "K")
elif (choice==3):
    print(celcius, "°C =", reaumur, "°Ré")
elif (choice==4):
    print(celcius, "°C =", farenheit, "°F")
    print(celcius, "°C =", kelvin, "K")
    print(celcius, "°C =", reaumur, "°Ré")
else:
    print("Błąd!")


