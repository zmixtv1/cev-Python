num = int(input("Você quer a tabuada de? "))

if num<1 or num>10:
   print ("Informe um número entre 1 e 10.")
else:
   for contar in range(0, 11):
       print (num, "x", contar, "=", (num*contar))
