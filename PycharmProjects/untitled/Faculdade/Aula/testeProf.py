#mostrando o mês

# Solicita a mês
mes = float(input('Qual o mês atual? '))

# Verifica se é Verão
verao = 1 <= mes <= 3

# Verifica se é Outono
outono = 4 <= mes <= 6

# Verifica se é Inverno
inverno = 7 <= mes <= 9

# Verifica se é Primavera
primavera = 10 <= mes <= 12

# Mostra qual a estação atual
print(f'Verão: {verao}\nOutono: {outono}\nInverno: {inverno}\nPrimavera: {primavera}\n')


#um maior que o outro
n1 = int(input("Informe o primeiro número:"))
n2 = int(input("Informe o segundo número:"))

print ("Primeiro > Segundo:", n1 > n2)
print ("Segundo > Primeiro:", n2 > n1)
print ("Primeiro = Segundo:", n1 == n2)