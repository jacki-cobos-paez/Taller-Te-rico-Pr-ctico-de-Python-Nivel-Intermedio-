numeros = [3, 7, 12, 18, 21, 30]

pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print("Números pares:", pares)