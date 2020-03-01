#abrir un archivo, convertirlo a mayusculas, quitarle el doble enter e imprimir
fname=input("Enter file name; ")
fh= open(fname)
for line in fh:
    line=line.rstrip()
    line=line.upper()
    print(line)