# Lucas Hanson - Homework 2 - Problem 3

x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
z = int(input("Enter a number for z: "))

if x%2 == 0:
	x = 0
if y%2 == 0:
	y = 0
if z%2 == 0:
	z = 0
	
if x == 0 and y == 0 and z == 0:
	print("Neither x, y, or z is an odd number.")

if x > y and x > z:
	greatest = x
elif y > x and y > z:
	greatest = y
elif z > x and z > y:
	greatest = z
if x != 0 or y != 0 or z != 0:
	print('The greatest odd number of the three is: %d' % greatest)




	
