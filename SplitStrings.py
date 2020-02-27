#Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#Examples:
#solution('abc') # should return ['ab', 'c_']
#solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    answer=[]
    if len(s)%2 != 0:
        s+="_"
    for number in range(0, len(s), 2):
        answer.append(s[number:number+2] )
    return answer