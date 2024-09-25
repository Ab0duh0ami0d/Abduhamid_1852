def Funksiya(dic,ls):
    for x in ls:
        dic[x] = 0
    for i in ls:
        dic[i] += 1    
    return dic
dic = dict()
ls = list(map(int,input("Butun sonlar kriting >>> ").split()))
print(Funksiya(dic,ls))    