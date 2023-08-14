a = int(input("Informe um número inteiro: "))
print(a)

a +=1
print(a)

a +=1
print(a)

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()