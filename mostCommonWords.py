fhand=open(mbox-short.txt)
count= dict()
for line in fhand:
    line=line.split()
    for word in line:
        count[word]= count.get(word,0)+1

lst= list()
for key, value in count:
    temptouple= (value, key)
    lst.append(temptouple)

# version corta del for pasado
#lst=sorted([(v,k) for k,v in count.items()])

lst=sorted(lst, reverse=true)

for val, key in lst[:10]:
    print(key, val)
