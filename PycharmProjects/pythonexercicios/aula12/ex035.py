print('-=-' * 20)
print('analisador de triângulos')
print('-=-' * 20)
s1 = int(input('Primeiro Segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro Segmento'))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 +s2:
    print('Os segmentos acima Podem formar triangulos!!')

