#!/usr/bin/python
"""identify a type of triangle"""
def classify_triangle(a_side, b_side, c_side):
    """checks type of triangle"""
    if a_side >= b_side - c_side:
        if b_side >= a_side - c_side:
            if c_side >= a_side + b_side:
                return "Not a triangle!"
    if a_side**2 + b_side**2 == int(c_side**2):
        if a_side != b_side and b_side != c_side and a_side != c_side:
            return "This triangle is a right scalene triangle!"
        return "This triangle is a right isoceles"
    if a_side != b_side and b_side != c_side and a_side != c_side:
        return "This triangle is scalene!"
    if a_side == b_side and b_side == c_side:
        return "This triangle is equilateral!"
    if a_side == b_side or b_side == c_side or c_side == a_side:
        return "This triangle is isoceles!"
print(classify_triangle(1, 1, 1))
# print(classify_triangle(2, 2, 1))
print(classify_triangle(3, 4, 5))
print(classify_triangle(2, 5, 6))
print(classify_triangle(50, 1, 100))
print(classify_triangle(12, 12, 12*(2**(1/2))))
# print(int(12*(2**(1/2))))
