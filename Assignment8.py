text = "X-DSPAM-Confidence:    0.8475";
sppos=text.find(" ")
numbers=text[sppos:]
total=numbers.strip()
result=float(numbers)
print(result)