import re

# Função para ler a entrada do código fonte
def ler_codigo_fonte():
    codigo_fonte = input("Digite a expressão de três operandos: ")
    return codigo_fonte

# Função para reconhecer os caracteres na sintaxe da expressão
def analisar_lexema(codigo_fonte):
    tokens = re.findall(r'[a-zA-Z]+|\d+|\S', codigo_fonte)
    numero_operandos = 0
    for token in tokens:
        if token.isalnum():
            numero_operandos += 1

    if numero_operandos > 4:
        print("Erro: Mais de três operandos encontrados.")
        exit()

    return tokens

# Função para criar e exibir a tabela de símbolos
def criar_tabela(tokens):
    tabela = []
    for token in tokens:
        if token.isalpha():
            tipo = 'IDENTIFICADOR'
        elif token.isdigit():
            tipo = 'NUMERO'
        elif token == '=':
            tipo = 'OPERADOR de atribuição'
        else:
            tipo = 'OPERADOR'
        tabela.append((token, tipo))
    return tabela

# Função para mostrar a execução da identificação dos tokens
def mostrar_execucao(tokens):
    print("EXECUÇÃO DA IDENTIFICAÇÃO DOS TOKENS:")
    for token in tokens:
        print("Lexema:", token[0], "\tTipo:", token[1])

# Função principal
def main():
    # Função 1: Ler a entrada do código fonte
    codigo_fonte = ler_codigo_fonte()

    # Função 2: Reconhecer os caracteres na sintaxe da expressão
    tokens = analisar_lexema(codigo_fonte)

    # Função 3: Criar e exibir a tabela de símbolos
    tabela_simbolos = criar_tabela(tokens)
    print("\nTABELA DE SÍMBOLOS:")
    for entrada in tabela_simbolos:
        print("Lexema:", entrada[0], "\tTipo:", entrada[1])

    # Função 4: Mostrar a execução da identificação dos tokens
    mostrar_execucao(tabela_simbolos)

if __name__ == "__main__":
    main()
