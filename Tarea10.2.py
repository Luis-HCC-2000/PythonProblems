name=input("Ingresar nombre del archivo")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
diccionario=dict()
for lines in handle:
    lines=lines.strip()
    if lines.startswith("From"):
        lines=lines.split()
        if len(lines)>4:
            palabra=lines[5]
            palabra=palabra.split(":")
            correcta=palabra[0]
            diccionario[correcta]=diccionario.get(correcta,0)+1
bien=diccionario.items()
bien=sorted(bien)
for k,v in bien:
    print(k,v)


#texto="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
#texto=texto.strip()
#lina=texto.split()
#print(lina[5])
