print("como te llamas?")
nombre = input()
print(f"hola {nombre}")
edad = input("que edad tienes?\n")
edad = int(edad)
print(f"ahh entonces tienes {edad} años dentro de 20 años tendras {edad + 20} años")

print("obtener varias cosas")

country, city = input("ingresa tu pais y ciudad separados por una coma: ").split(",")
print(f"pais: {country} ciudad: {city}")
