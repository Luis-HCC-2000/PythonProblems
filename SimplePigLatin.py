#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    text=text.split()
    correct=[]
    for index,word in enumerate(text):
        correct.append(word) if (index==(len(text)-1) and len(word)==1) else correct.append(word[1:]+word[0]+"ay")
    return " ".join(correct)