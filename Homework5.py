largest=None
smallest=None
while True:
    num=input("Ingresa número: ")
    if num=="done":
        break
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest=num
    elif smallest>num:
        smallest=num
    if largest is None:
        largest=num
    elif largest<num:
        largest=num
print("Maximum is", largest)
print("Minimum is", smallest)