ls = [{"Madel": "X7"}, {"Yil": 2001},{"Madel": "XL"}, {"yil": 1999},{"Madel": "Gt"}, {"yil": 2005},{"Madel": "LR2"}, {"yil": 2015},{"Madel": "XT7"}, {"yil": 2024}]

def Yil(data):
    return data[1]

yil = []
for i in range(1, len(ls), 2):
    kalt = 'Yil' if 'Yil' in ls[i] else 'yil'
    yil.append((ls[i-1], ls[i][kalt]))

yil.sort(key = Yil)
Natija = []
for madel, y in yil:
    Natija.append(madel)
    Natija.append({"Yil": y})

print(Natija)
