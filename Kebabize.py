#Modify the kebabize function so that it converts a camel case string into a kebab case.
#kebabize('camelsHaveThreeHumps') // camels-have-three-humps
#kebabize('camelsHave3Humps') // camels-have-humps
#Notes:
#the returned string should only contain lowercase letters

def kebabize(string):
    import re
    string=(re.sub(r"([A-Z])", r"-\1",string)).lower()
    string=re.sub(r"([0-9])", r"",string)
    if string == "": return string
    if string[0]=="-": string=string[1:]
    return string