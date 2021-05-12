print('-=-' * 20)
print('analisador de triângulos')
print('-=-' * 20)
s1 = int(input('Primeiro Segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro Segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 +s2:
    print('Os segmentos acima Podem formar triangulos!!')
    if s1 == s2 == s3:
        print("Este triangulo é Equilatero!")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Este triangulo é Isóceles!")
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print("Este triangulo é Escaleno!")
else:
    print("Os segmento não podem formar um triangulo!")