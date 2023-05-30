from math import pi

def circle_draw(r):
    if type(r) is not int and type(r) is not float:
        raise TypeError("The radius is not an integer or a float!")
    if r < 0 :
        raise ValueError("The radius cannot be negative!")
    return pi*(r**2)
