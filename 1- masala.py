def Funksiya(N):
    ls = ["A", "b", "d", "u", "h", "a", "m", "i", "d", "2","0","0","0","-","y","i","l"]
    
    return [ls[i:i + n] for i in range(0,len(ls),n)]

n = int(input("Bitta butun son kriting >>> "))
Natija = Funksiya(n)
print(Natija)