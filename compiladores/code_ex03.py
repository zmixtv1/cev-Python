numeros = range(48, 57)
barra_abrir = 40
barra_fechar = 41
multiplicacao = 42
soma = 43
subtracao = 45
divisao = 47
ponto = 46
espaco = 32

def calculadora_ascii(caracteres):
    try:
        resultados = [ord(c) for c in caracteres]
        return resultados
    except TypeError:
        return "Erro: Forneça uma string de caracteres."

def main():
    caracteres = input("Digite uma string de caracteres: ")
    resultados = calculadora_ascii(caracteres)
    
    print("Valores ASCII correspondentes (incluindo espaços):")
    for i, caractere in enumerate(caracteres):
        if resultados[i] in range(48, 57):  
            print(f"{caractere}: número real")
        elif resultados[i] == barra_fechar:
            print(") => fecha parênteses")
        elif resultados[i] == multiplicacao:
            print("* => operador de multiplicação")
        elif resultados[i] == soma:
            print("+ => operador de soma")
        elif resultados[i] == subtracao:
            print("- => operador de subtração")
        elif resultados[i] == divisao:
            print("/ => operador de divisão")
        elif resultados[i] == barra_abrir:
            print("( => abre parênteses")
        elif resultados[i] == espaco:
            print("____ => espaço em branco")
        else:
            print('elemento desconhecido')

if __name__ == "__main__": 
    main()
