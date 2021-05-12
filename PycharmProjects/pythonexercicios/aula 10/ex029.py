velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('MULTADO! Você exedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'A multa é de {multa}')

print('Tenha um bom dia. Dirija com segurança!!')