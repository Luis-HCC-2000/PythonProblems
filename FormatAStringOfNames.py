#Given: an array containing hashes of names

#Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

#Example:

#namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

#namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

#namelist([ {'name': 'Bart'} ])
# returns 'Bart'

#namelist([])
# returns ''

def namelist(names):
    allNames=[]
    if len(list(names))>1:
        for name in names:
            allNames.append(name.get("name"))
        lastName=allNames[-1]
        del allNames[-1]
        res=", ".join(allNames) + " & " + lastName
    elif len(list(names))==1:
        for name in names:
            allNames.append(name.get("name"))
        res=allNames[0]
    else:
        return ""
    return res