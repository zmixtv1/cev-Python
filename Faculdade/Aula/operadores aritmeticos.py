altura = float(input('Qual a altura do triângulo?'))
largura = float(input('Qual a base do triangulo?'))
base = (altura * largura) / 2
print(f'A área do triangulo é de {base}')


reais = int(input('Me fale um valor em Reais!:'))
print(reais)
dolares = (reais / 5.65)
euro = (reais / 6.65)
print('O valor da moeda em Dolares é: {:.2f} \nE o valor da moeda em euros é: {:.2f}'.format(dolares, euro))

salario = float(input('Me fale um salario:'))
fgts = (salario * 0.08)
print('você deve depositar {} reais , para o FGTS!!'.format(fgts))

a = float(input('Qual a sua altura? : '))
p = float(input('Qual é o seu peso? : '))
imc = p / (a ** 2)

print('O seu indice de massa corporal é de {:.2f}!!'.format(imc))
