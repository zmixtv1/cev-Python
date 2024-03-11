numeros = range( 48, 57)
barra_abrir = 40
barra_fechar = 41
multiplicacao = 42
soma = 43
subtracao = 45
divisao = 47
ponto = 46
espaco = 160

def calculadora_ascii(caracteres):
    try:
        resultados = [ord(c) for c in caracteres if not c.isspace()]
        return resultados
    except TypeError:
        return "Erro: Forneça uma string de caracteres."

def main():
    caracteres = input("Digite uma string de caracteres: ")
    resultados = calculadora_ascii(caracteres)
    
    print("Valores ASCII correspondentes (ignorando espaços):")
    for i, caractere in enumerate(caracteres):
        if not caractere.isspace():
            print(resultados.pop(0))
            if resultados.pop(0) in range(48, 57):  
                c = 'número real'
                print(f"{caractere}: numero real")
            elif resultados.pop(0) == barra_fechar:
                print(") => fecha parênteses")
            elif resultados.pop(0) == multiplicacao:
                print("* => operador de multiplicação")
            elif resultados.pop(0) == soma:
                print("+ => operador de soma")
            elif resultados.pop(0) == subtracao:
                print("- => operador de subtração")
            elif resultados.pop(0) == divisao:
                print("/ => operador de divisão")
            elif resultados.pop(0) == barra_abrir:
                print("(  => abre parênteses")
            else:
                print("outro")


if __name__ == "__main__": 
    main()

