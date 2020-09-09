def classify_triangle(a,b,c):
    #Removing check for valid triangle as intended bug.
    #if (a+b<=c or a+c<=b or b+c<=b):
    #   return 'NotATriangle'
    result=""
    if((a*a+b*b)==(c*c)):
        result+='Right '
    if a==b or b==c or a==c:
        if a==c and a==b:
            result+='Equilateral'
        else:
            result+='Isoceles'
    else:
        result+="Scalene"
    return result