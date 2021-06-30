'''
numero=int(input("Qual o número entre 0 e 100? "))

if numero<0 or numero>100 :
   print("Eu não sou muito inteligente. Não conheço esse número. Meu mestre não me ensinou. Digo programou!")
else:
   ext=['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove']
   extDez = ['Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa', 'Cem']

   if numero<20:
       print("O número", numero, "por extenso é", ext[numero])
   else:
       if numero == 100:
           print ("O número", numero, "por extenso é", extDez[8])
       else:
           if numero % 10 == 0:
               print("O número", numero, "por extenso é", extDez[(numero // 10) - 2])
           else:
               print("O número", numero, "por extenso é", extDez[(numero // 10) - 2], 'e', ext[numero % 10])




--------------------------------------------------------------------------------------------------------------------------------------------




# ABCAB

 A - 2 ocorrência(s) que corresponde a 40 %
 B - 2 ocorrência(s) que corresponde a 40 %
 C - 1 ocorrência(s) que corresponde a 20 %


print('Digite uma frase qualquer:')
f = input()

tab = []
for i in range(256):
    tab.insert(i, 0)
print (tab)

for c in f:
    tab[ord(c)] += 1
print(tab)

soma = 0
for i in range(256):
    if tab[i] != 0:
        porc = tab[i] * 100 / len(f)
        print (chr(i), '-', tab[i], 'ocorrência(s) que corresponde a', porc, '%')
        soma += porc

print ('Total=', soma)

# len(f) -- 100%
# tab[i] -- p
# p * len(f) = tab[i] * 100
# p = tab[i] * 100 / len(f)
'''