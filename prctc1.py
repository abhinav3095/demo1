
#1 radius of circle

r= float(input("enter the radius: "))
a= 22/7*(r**2)
print("area of the circle: " ,a)

#2 fahrenheit to degree


fn = float(input("temperatue of city in fahrenheit"))
ct = ((fn - 32) *5)/9
print("temperature in degree" , ct)


#3 simple calculator

num_1 = int(input("enter first number: "))
num_2 = int(input("enter second number: "))

print(num_1, "+", num_2, "=", (num_1 + num_2))
print(num_1, "-", num_2, "=", (num_1 - num_2))
print(num_1, "*", num_2, "=", (num_1 * num_2))
print(num_1, "/", num_2, "=", (num_1 / num_2))


#4  the square root

import math
a = int(input("enter the number"))
print(math.sqrt(a))



#5 quadratic equation

import math

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))
d = math.sqrt(b**2 - 4 * a * c)

x= ((-b + d)/ 2 * a)
y= ((-b - d)/ 2 * a)


print( x , y)


#6 area of triangle

import math
a= int(input("enter the first side: "))
b= int(input("enter the second side: "))
c= int(input("enter the third side: "))

s = ((a + b + c)/ 2)
x = (s * (s - a) * (s - b) * (s - c))
print(math.sqrt(x))


#7calculate the sum of its digits

su = 0
a = int(input("enter the 5 digit number: "))

b = a % 10
su = su + b
c = (a // 10) % 10
su = su + c
d = (a // 100) % 10
u = su + d
e = (a // 1000) % 10
su = su + e
f = (a // 10000)
su = su + f


print(su)


#8  string in a specific format
print("Twinkle, twinkle, little star,\n\thow i wonder what you are!\n\t\tup above the world so high,\n\t\tlike a diamond in thesky.\nTwinkle, twinkle, little star,\n\thow i wonder what you are!")


#9  display your details
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
address = str(input("Enter your address: "))

print("Name: %s\nAge: %d\nAddress: %s "%(name, age , address))







