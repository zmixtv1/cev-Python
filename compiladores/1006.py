def analisador_lexico_e_sintatico(expressao):
    tabela_simbolos = []
    lexemas = expressao.split()
    tokens = []
    erros_sintaticos = []
    contador_identificadores = 0

    operadores_aritmeticos = ["=", "+", "-", "*", "/"]
    operadores_relacionais = ["==", "!=", ">", ">=", "<", "<="]

    for lexema in lexemas:
        if lexema.isalnum() and not lexema.replace('.', '', 1).isdigit():
            contador_identificadores += 1
            if contador_identificadores > 3:
                erros_sintaticos.append("Erro: foram encontrados mais de um operandos e operadores antes do enunciado de atribuição.")
            tokens.append("Identificador")
        elif lexema in operadores_aritmeticos:
            tokens.append("Operador Aritmético")
        elif lexema in operadores_relacionais:
            tokens.append("Operador Relacional")
        elif lexema.replace('.', '', 1).isdigit():
            if '.' in lexema:
                tokens.append("Número decimal")
            else:
                tokens.append("Número inteiro")
        elif lexema == ";":
            tokens.append("Delimitador")
        else:
            tokens.append("Desconhecido")

    tabela_simbolos = list(zip(lexemas, tokens))

    for i in range(len(lexemas) - 1):
        if lexemas[i].isalnum() and lexemas[i+1].isalnum() and not lexemas[i].isdigit() and not lexemas[i+1].isdigit():
            erros_sintaticos.append("Erro: foram encontradas duas variáveis seguidas e separadas por espaço em branco")
        elif lexemas[i] in operadores_aritmeticos and lexemas[i+1] in operadores_aritmeticos:
            erros_sintaticos.append("Erro: foram encontrados dois operadores aritméticos seguidos e separados por espaço em branco")
        elif lexemas[i] in operadores_relacionais and lexemas[i+1] in operadores_relacionais:
            erros_sintaticos.append("Erro: foram encontrados dois operadores relacionais seguidos e separados por espaço em branco")

    return tabela_simbolos, erros_sintaticos


expressao = input("Digite a expressão: ")
tabela_simbolos, erros_sintaticos = analisador_lexico_e_sintatico(expressao)
print("\nTabela de Símbolos:")
for lexema, token in tabela_simbolos:
    print(f"{lexema}: {token}")

if not erros_sintaticos:
    print("\nExpressão correta.")
else:
    print("\nErros sintáticos encontrados:")
    for erro in erros_sintaticos:
        print(erro)
        
        
        # Função para verificar se o caractere é um operador
def is_operator(char):
    return char in ['+', '-', '*', '/']

# Função para verificar a precedência dos operadores
def precedence(operator):
    if operator in ['+', '-']:
        return 1
    elif operator in ['*', '/']:
        return 2
    return 0

# Função para converter a expressão infix para pós-fixa
def infix_to_postfix(expression):
    postfix = ""
    stack = []  # Usaremos uma lista como pilha

    for char in expression:
        if char.isdigit():
            postfix += char
        elif char == ' ':
            continue
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Remover '(' da pilha
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix += stack.pop()
            stack.append(char)

    # Adicionar os operadores restantes na pilha ao resultado
    while stack:
        postfix += stack.pop()

    return postfix

# Função principal para testar
def main():
    infix_expression = input("Digite a expressão infix: ")
    postfix_expression = infix_to_postfix(infix_expression)
    print("Expressão pós-fixa:", postfix_expression)

if _name_ == "_main_":
    main()