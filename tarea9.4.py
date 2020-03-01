name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dictionary = dict()
for line in handle:
    words= line.split()
    index = line.find("From ")
    if index > -1:
        word = words[index+1]
        dictionary[word] = dictionary.get(word, 0)+1
maxvalue=0
for keys in dictionary:
    values= dictionary[keys]
    if maxvalue==0 or dictionary[keys] > maxvalue:
        maxvalue= values
        maxkey= keys
print(maxkey, maxvalue)