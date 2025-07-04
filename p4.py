#Python program to find  the area of (i)Rectangle (ii)Triangle (iii)Circle
#(i)Python program to find the area of rectangle
print("(i)Python program to find the area of rectangle")
length=float(input("Enter the length of the rectangle in cm: "))
breadth=float(input("Enter the breadth of the rectangle in cm: "))
area=length*breadth
print("The area of the rectangle with length",length,"cm and breadth",breadth,"cm is",area,"cm")
#(ii)Python program to find the area of triangle
print("(ii)Python program to find the area of triangle")
base=float(input("Enter the base of the triangle in cm: "))
height=float(input("Enter the height of the triangle in cm: "))
area=(base*height)/2
print("The area of the triangle with base",base,"cm and height",height,"cm is",area,"cm")
#(iii)Python program to find the area of circle
print("(iii)Python program to find the area of circle")
import math as m
radius=float(input("Enter the radius of the circle in cm: "))
area=m.pi*radius*radius
print("The area of the circle with radius",radius,"cm is",area,"cm")