def mixed_fraction(s):
    from fractions import Fraction
    divided=s.split("/")
    numerator, denominator= abs(int(divided[0])), abs(int(divided[1]))
    residual, integer=numerator%denominator, int(numerator/denominator)
    fraction=str(Fraction(residual,denominator))
    if integer==0: integer=""
    if fraction=="0": fraction=""
    result=str(integer)+" "+fraction
    if result==" ": result="0"
    sign=int(divided[0])*int(divided[1])
    result=result.strip()
    if sign<0: result="-"+result
    return result