#!/usr/bin/python3
import math

def Circle(radius):
    area = math.pi * radius**2
    return area

def Rectangle(length, width):
    area = length * width
    return area

def Square(length):
    area = length * length
    return area

def get_shape():
    shape = input("Enter the shape: ")
    return shape
#shape = input("Enter the shape: ")
shape = get_shape().lower()

if (shape == "circle"):
    radius = float(input("Enter the raduis: "))
    #area = math.pi*radius**2
    print("area of the circle is: ", round(Circle(radius), 2))

elif (shape == "rectangle"):
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    #area = length * width
    print("The area of the rectangle is: ", round(Rectangle(length, width), 2))

elif (shape == "square"):
    length = float(input("Enter the length: "))
    # area = length * length
    print("The area of the square is: ", round(Square(length),2))
else:
    print("Unknown shape")
