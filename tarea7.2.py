title = input("Indicate the file name")
handling = open(title)
lines = 0
total = 0
for line in handling:
    line=line.upper()
    line = line.strip()
    find = line.find("X-DSPAM-CONFIDENCE:")
    if find > -1:
        lines += 1
        total += float(line[19:])
avg = total/lines
print("Average spam confidence:", avg)
