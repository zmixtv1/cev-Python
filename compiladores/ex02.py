maiuscula = input(str("Digite Tudo minusculo: "))
print(f"\n saída : {maiuscula.upper()}\n ")

minusculo = input(str("Digite Tudo Maiusculo: "))
print(f"\n saída : {minusculo.lower()} \n \n")

def converter_maiuscula_minuscula(texto):
    resultado = ""
    for char in texto:
        if char.isupper():
            resultado += char.lower()
        elif char.islower():
            resultado += char.upper()
        else:
            resultado += char
    return resultado

def main():
    entrada = input("Digite uma string com letras maiúsculas e minúsculas: ")
    resultado_equivalentes = converter_maiuscula_minuscula(entrada)
    print(f"\n Saída com caracteres equivalentes:{resultado_equivalentes} \n")

if __name__ == "__main__":
    main()
