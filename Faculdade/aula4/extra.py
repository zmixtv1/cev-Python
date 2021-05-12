# Recebe a frase
frase = input('Insira a frase: ')

# Lista de consoantes
a = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
# Lista de vogais
b = ['a', 'e', 'i', 'o', 'u']


# Função para retirar os carácteres especiais (MUITO CHATO, tive que pegar um por um)
def acentos(c):
    d = ['à', 'á', 'â', 'ã', 'ä', 'å']
    e = ['è', 'é', 'ê', 'ë']
    f = ['ì', 'í', 'î', 'ï']
    g = ['ò', 'ó', 'ô', 'õ', 'ö']
    h = ['ù', 'ú', 'û', 'ü']
    i = ['ý', 'ÿ']
    j = ['ß']
    k = ['ñ']
    l = ['ç']
    for z in c:
        if z in d:
            z = 'a'
            return z
        elif z in e:
            z = 'e'
            return z
        elif z in f:
            z = 'i'
            return z
        elif z in g:
            z = 'o'
            return z
        elif z in h:
            z = 'u'
            return z
        elif z in i:
            z = 'y'
            return z
        elif z in j:
            z = 'ss'
            return z
        elif z in k:
            z = 'n'
            return z
        elif z in l:
            z = 'c'
            return z
        else:
            return z


# Checa se a frase não é nula
if frase != '' and frase != ' ':
    # Variáveis de espaços, vogais e consoantes
    espacos = 0
    vogais = 0
    consoantes = 0
    # Varredura nos elementos + retira o maiúsculo
    for elemento in frase.lower():
        # Se for espaço:
        if acentos(elemento) == ' ':
            espacos += 1
        # Se for vogal:
        elif acentos(elemento) in b:
            vogais += 1
        # Se for consoante:
        elif acentos(elemento) in a:
            consoantes += 1

    # Printa o resultado final
    print(f'Número de espaços: {espacos}\nNúmero de vogais: {vogais}\nNúmero de consoantes: {consoantes}')

# Se a frase for nula:
else:
    print('Insira uma frase válida!')