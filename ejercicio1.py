numeros = []

for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

mayor = max(numeros)
menor = min(numeros)
promedio = sum(numeros) / len(numeros)

print("Número mayor:", mayor)
print("Número menor:", menor)
print("Promedio:", promedio)
