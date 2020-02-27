#Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

#each taken only once - coming from s1 or s2.
#Examples:
#a = "xyaabbbccccdefww"
#b = "xxxxyyyyabklmopq"
#longest(a, b) -> "abcdefklmopqwxy"
#a = "abcdefghijklmnopqrstuvwxyz"
#longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(s1, s2):
    characters = list(s1 + s2)
    characters.sort()
    res = []
    for character in characters:
        if character not in res:
            res.append(character)
    return "".join(res)
