'''pessoas = {"nome": "Gustavo", "Sexo": "M", "Idade": 22}
for k, v in pessoas.items():
    print(f"{k} = {v}")
'''
estado = dict()
brasil = list()
for c in range(0,3):
    estado["uf"] = str(input("Unidade federativa: ")).capitalize()
    estado["Sigla"] = str(input("Sigla do Estado: ")).capitalize()
    brasil.append(estado.copy())
for e in brasil:
    '''
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}.")
    '''
    for v in e.values():
        print(v, end=" ")
    print("fim")
