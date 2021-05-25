'''lanche = ("hamburguer", "suco", "pizza", "pudim", "batata frita")
for cont in range(0, len(lanche)):
    print(f"eu vou comer {lanche[cont]}!")

for comida in lanche:
    print(f"eu vou conmer {comida}!")
'''
'''
a = (2, 5 ,4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(2, 1))
'''
'''
pessoa = ("Gustavo", 39, "M", 99.88)
del pessoa
print(pessoa)
'''
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(6)
num.sort(reverse=True)
num.insert(2, 0)
print(num)
print(f"Essa lista tem {len(num)} elementos")
'''
'''
valores = [1, 4]
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final do programa!")
'''
valores = list()

for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista")

print(valores)

