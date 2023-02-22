import math


# method for calculating volume of sphere
def volume_of_sphere(radius):
    return (4 * math.pi * radius * radius * radius) / 3


# method for calculating volume of cylinder
def volume_of_cylinder(radius, height):
    return math.pi * radius * radius * height


# method for calculating volume of cone
def volume_of_cone(radius, height):
    return (math.pi * radius * radius * height) / 3


# method for calculating volume of pyramid
def volume_of_pyramid(length, width, height):
    return (length * width * height) / 3
