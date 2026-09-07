KELVIN_OFFSET = 273.15

celsius = float(input("Suhu Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + KELVIN_OFFSET

print("\n===== KONVERSI SUHU =====")
print(f"Celsius    : {celsius:.2f} °C")
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")