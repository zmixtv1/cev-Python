cid = str(input('Qual a cidade em que você mora? : ')).strip().capitalize()
print('O nome da sua cidade comessa com santo: {}'.format(cid[:5] == 'Santo'))