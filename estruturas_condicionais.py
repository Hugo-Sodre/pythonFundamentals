import sys

saldo = 2000.0
saque = float(input("Informe o valor do saque : "))

if saldo >= saque:
    print("Realizando saque! ")

if saldo < saque:
    print("Saldo insuficiente!")



opcao = int(input("Informe uma opção : [1] Sacar \n[2] Extrato"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque : "))

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    sys.exit("Opção inválida")


MAIOR_IDADE = 18
IDADE_ESPECIAL = 12
idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")



if idade >= MAIOR_IDADE:
    print("Maior da idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH")


