frase ='curso em video python'
#Quantidade de caracteres, (comprimento)!
print(len(frase))
#Quantas vezes aparece na frase!
print(frase.count('o'))
#quantas vezes ele encontrou (mostra o início)!
print(frase.find('deo'))
#Qundo não encontrar nada mostrara (-1)!
print(frase.find('android'))
#pergunta se tem a palavra dentro da frase!
print('curso'in frase)
#troca a uma palavra pela outra!
print(frase.replace('python','Android'))
#Transformar as frases em maiusulo!!
print(frase.upper())
#Transformar as frases em minusculo!!
print(frase.lower())
#Transformar tudo em minusculo só o primeiro maiusculo
print(frase.capitalize())
#todos os caracteres depois do espaço fica maiusculo
print(frase.title())
#remove todos os espaços sobrando ! colocar o r remove só da direira e l da esquerda!!
print(frase.strip())
#Dividir os espaços (lista separadas por cada paalavra)
print(frase.split())
#juntar todos os separadores com a separação indicada
print('-'.join(frase))
