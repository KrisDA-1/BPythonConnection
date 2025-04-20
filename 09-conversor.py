##Convert temperature
# from celsius to fahrenheit
temperatura=float(input("Ingresa la temperatura:")) 
escala=input("Es Farenheit(F) o es Celsius(C)?:").lower()
if escala=="f":
    celsius=(temperatura-32)/1.8
    print("La temperatura en Celsius es:",celsius)
elif escala=="c":
    farenheit=(temperatura*1.8)+32
    print("La temperatura en Farenheit es:",farenheit)
else:
    print("Escala no válida")