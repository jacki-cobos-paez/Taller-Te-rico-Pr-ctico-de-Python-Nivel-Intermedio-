palabra = input("Ingrese una palabra: ")
letra = input("Ingrese la letra que desea contar: ")

contador = 0

for l in palabra:
    if l == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces.")
