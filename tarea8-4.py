doc=open("romeo.txt")
lista=[]
minilista=[]
for line in doc:
    minilista=line.split()
    for word in (minilista):
        if word not in lista:
            lista.append(word)
lista.sort()
print(lista)