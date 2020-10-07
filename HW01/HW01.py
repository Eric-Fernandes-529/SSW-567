"""Homework assignment 1 for SSW 567"""
def classify_triangle(side_a,side_b,side_c):
    """Returns the type type of a triangle with sides a,b,c."""
    #Removing check for valid triangle as intended bug.
    if (side_a+side_b<=side_c or side_a+side_c<=side_b or side_b+side_c<=side_b):
       return 'NotATriangle'
    result=""
    if(side_a*side_a+side_b*side_b)==(side_c*side_c):
        result+='Right '
    if side_a==side_b or side_b==side_c or side_a==side_c:
        if side_a==side_c and side_a==side_b:
            result+='Equilateral'
        else:
            result+='Isoceles'
    else:
        result+="Scalene"
    return result
