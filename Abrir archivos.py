filename= input("Place the name and the extension of the file : ")
def linecounter(filename):
    try:
        loader=open(filename)
    except:
        print("Invalid file name")
        quit()
    count=0
    for line in loader:
        count += 1
    print("The number of lines in the file are:", count)
linecounter(filename)
def SearchNumberOfAuthors(filename):
    count=0
    try:
        file = open(filename)
    except:
        print("Invalid file name")
        quit()
    for line in file:
        line = line.lower()
        if line.find("from")> -1:
            count += 1
    print("The number of authors is: ", count)
SearchNumberOfAuthors(filename)