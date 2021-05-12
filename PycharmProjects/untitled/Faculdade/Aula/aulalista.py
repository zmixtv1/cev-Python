produtos = str
termos = 1
soma = ""
while produtos != "":
    produtos = input(str('Item ') + str(termos) + ':')
    soma = str(soma) + str(produtos)
    termos += 1

print('A lista é:a ', soma)