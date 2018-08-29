def classify_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        if a != b and b != c and a != c:
            return("This triangle is a right scalene triangle!")
        elif a==b or b==c or c==a:
            return("This triangle is a right isoceles")
    elif a != b and b != c and a != c:
        return("This triangle is scalene!")
    elif a==b and b==c:
        return("This triangle is equilateral!")
    elif a==b or b==c or c==a:
        return("This triangle is isoceles!")
    else:
        return("I don't think this triangle is special... or even a triangle")
