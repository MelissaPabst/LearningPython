current_time = int(input("What is the current time?"))
hours_to_wait = int(input("How many hours will you wait for the alarm to sound?"))

clock_hour = (current_time + hours_to_wait) % 24


print("When the alarm goes off, the clock will read:", clock_hour)
           
—

P = 10000
n = 12
r = 0.08

t = float(input("How many years will the money compound?"))

amount = (P)*((1+(r/n))**(n*t))

print("The final amount after", t, "years will be $", amount)
         
—

r = float(input("What is the radius of your circle?"))

area = 3.14*(r**2)

print("The area of a circle with a radius of", r, "is", area)

—

spins = input("How many times did you spin? (Enter a negative number for counter-clockwise spins) ")

degrees = (float(spins) * 360) % 360

print("You are facing", degrees, "degrees relative to north")

—

num_touchdowns = input("How many touchdowns were scored? ")
num_field_goals = input("How many field goals were scored? ")
td_points = input("How many points is a touchdown worth?")
fg_points = input("How many points is a field goal worth?")

total_score = int(td_points) * int(num_touchdowns) + int(fg_points) * int(num_field_goals)

print("The team has", total_score, "points")

—

clicks = int(input("How many clicks has the dial been turned?"))

clicks_diff = clicks % 50 

temperature = (40 + clicks_diff) 
print("The temperature is", temperature)

—

#ask what day the vacation starts
starting_day = int(input("If Sunday = 0, and so on, from 0 - 6, what day number will your vacation start on?"))

#ask how long they will be gone
days_away = int(input("How many days wil you be gone?"))

#compute the day of return
return_day = (starting_day + days_away) % 7

#print the day of return
print("You will return on", return_day)

—

import turtle
background = input("What color would you like for a background? Grey or Cyan?")

wn = turtle.Screen()
wn.bgcolor(background)        # set the window background color

tess = turtle.Turtle()
tess_color = input("What color would you like for tess to be? Pink or Red?")
tess.color(tess_color)              # make tess blue
tess_pensize = int(input("What size would you like to make tess? (Enter a number)"))
tess.pensize(tess_pensize)                 # set the width of her pen

tess.forward(150)
tess.left(120)
tess.forward(150)

wn.exitonclick() 

—

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()           # create alex

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin

alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()

—

number = int(input("Please enter an integer between 1 and 1000"))

for i in range (number):
    print("We like Python's turtles!")

—

for i in range (99, 1, -1):
    print( i, "bottles of beer on the wall,", i, "bottles of beer. You take one down, pass it around,", i -1, "bottles of beer on the wall.")

print("1 bottle of beer on the wall, 1 bottle of beer. You take one down, pass it around, and now there's no bottles of beer on the wall.")


—

for i in range(0, 51, 2):
    print(i)

__

for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    print("One of the months of the year is", month)

__

import turtle
wn = turtle.Screen()
wn.bgcolor("black")

Melissa = turtle.Turtle()
Melissa.color("hotpink")
Melissa.shape("circle")

for i in range(3):
    Melissa.forward(100)
    Melissa.left(120)
    
Bob = turtle.Turtle()
Bob.color("lime")
Bob.shape("arrow")

for i in range(4):
    Bob.forward(150)
    Bob.left(90)

Mikey = turtle.Turtle()
Mikey.color("red")
Mikey.shape("turtle")

for i in range(6):
    Mikey.forward(45)
    Mikey.left(360/6)

Abby = turtle.Turtle()
Abby.color("orange")
Abby.shape("square")

for i in range(8):
    Abby.forward(25)
    Abby.left(369/8)
    
wn.exitonclick()

—

number_sides = int(input("Let's build a regular polygon. How many sides will it have?"))
side_length = float(input("What are the lengths of the sides?"))
side_color = input("What color are the sides to be drawn in?")
fill_color = input("What is the color of the polygon?")

__

import turtle
wn = turtle.Screen()

pirate = turtle.Turtle()

pirate.penup()
pirate.forward(100)
pirate.pendown()

for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(angle)
    pirate.forward(100)
    
wn.exitonclick()

—

import turtle
wn = turtle.Screen()

star = turtle.Turtle()

for i in range(5):
    star.forward(100)
    star.right(144)

—

import turtle
wn = turtle.Screen()
wn.bgcolor("lime")

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.color("blue")
tommy.speed(20)
tommy.penup()

tommy.stamp()
for hours in range(12):
    tommy.forward(120)
    tommy.pendown()
    tommy.forward(10)
    tommy.penup()
    tommy.forward(20)
    tommy.stamp()
    tommy.forward(-150)
    tommy.right(360/12)
    
wn.exitonclick()

—

import turtle
wn = turtle.Screen()
wn.bgcolor("black")

picture = turtle.Turtle()
picture.color("HotPink", "blue")
picture.hideturtle()
picture.pensize(0.5)
picture.speed(20)

picture.begin_fill()
for i in range (200):
    picture.forward(i)
    picture.right(110)

picture.end_fill()

wn.exitonclick()

—

import turtle
wn = turtle.Screen()

Lisa = turtle.Turtle()

x = Lisa

print(type(x))
print(type(Lisa))

—

import turtle
wn = turtle.Screen()

num_legs = int(input("How many legs will your sprite have?"))

sprite = turtle.Turtle()
sprite.shape("circle")
sprite.hideturtle()

for i in range (num_legs):
    sprite.forward(150)
    sprite.forward(-150)
    sprite.left(360/num_legs)
    
wn.exitonclick() 
 
—

import random

for i in range(10):
    print(random.randrange(0, 20))

—

import random

for i in range(10):
    print(random.randrange(25, 35))

—

import math

side1 = 3
side2 = 4
hypotenuse = math.hypot(side1,side2)
print(hypotenuse)

—

import math

approx_pi = 355/113
print(approx_pi)

print(math.pi)

—

nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in nums:
    print(i)
for i in nums:
    print("The square of", i, "is", i**2)

—

import turtle
import random

win = turtle.Screen()

# create 2 turtles
zach = turtle.Turtle()
jesse = turtle.Turtle()

# speed them up!
zach.speed(10)
jesse.speed(10)

jesse.color("green")
zach.color("orange")

jesse.penup()
zach.penup()
jesse.goto(-100, 0)
zach.goto(-100, 0)
jesse.pendown()
zach.pendown()

# make them walk randomly, loop variable represents distance to travel forward
for distance in range(0,50,2): # generates [0,2,4,6,8,10,12,...46,48]

    # create a random angle for each turtle
    zach_angle = random.randrange(0,181)
    jesse_angle = random.randrange(0,181)

    # turn each turtle in that random direction
    zach.left(zach_angle)
    jesse.left(jesse_angle)

    # move each turtle forward by distance
    zach.forward(distance)
    jesse.forward(distance)

#doug code
# for i in range(10):
    #randomly choose a direction
    
    #direction = random.randrange(-45, 45)
    #direction2 = random.randrange(-45, 45)
        
    #jesse.left(direction)
    #zach.left(direction2)
    
    #move in that direction
    
    #distance = random.randrange(25, 25)
    #distance2 = random.randrange(25, 25)
    
    #jesse.forward(distance)
    #zach.forward(distance2)
    
win.exitonclick()    


—

import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3. Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4. Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

# your code goes here

# 1. single call to forward
#lance_distance = random.randrange(0, 200)
#andy_distance = random.randrange(0, 200)

#lance.forward(lance_distance)
#andy.forward(andy_distance)

#OR

#lance.forward(random.randrange(100))
#andy.forward(random.randrange(100))

#2. for loop

turns = random.randrange(0, 25)

for distance in range(turns):
    lance.forward(random.randrange(0, 25))
    andy.forward(random.randrange(0, 25))
    
#OR

#for distance in range(random.randrage(0, 25))
    #lance.forward(random.randrange(0, 25))
    #andy.forward(random.randrange(0, 25))
                      
# 3. other

#for turtle in ["lance", "andy"]:
    #lance.forward(random.randrange(0, 200))
    #andy.forward(random.randrange(0, 200))
                       
wn.exitonclick()

__

import turtle

def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("hotpink")
    alex.pensize(4)
    alex.penup()
    alex.goto(-100, 0)
    alex.pendown()
    
    for i in range(5):
        draw_square(alex,20)
        alex.penup()
        alex.forward(40)
        alex.pendown()

    wn.exitonclick()

if __name__ == "__main__":
    main()

—

import turtle

def draw_square(t, sz):
    
    for i in range(4):
        t.forward(sz)
        t.left(90)

        
def main ():        
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    pinky = turtle.Turtle()
    pinky.color("hotpink")
    pinky.pensize(3)
    
    size = 20
    x = 0
    y = 0
    for i in range(5):
        draw_square(pinky, size)
        size = size + 20
        pinky.penup()
        x = x - 10
        y = y - 10
        pinky.goto(x, y)
        pinky.pendown()


    window.exitonclick()
    
    
if __name__ == "__main__":
    main()

—

import turtle

def draw_poly(t, sides, side_length):
    for i in range(sides):
        t.forward(side_length)
        t.left(360/sides)
    
    
def main():
    win = turtle.Screen()
    win.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.color("hotpink")
    tess.pensize(3)
    
    draw_poly(tess, 8, 50)
    
    win.exitonclick()
    
    
if __name__ == "__main__":
    main()  

—

import turtle, sys

def draw_spiral(t, angle, length):
        t.right(angle)
        t.forward(length)
        
def main():
    win = turtle.Screen()
    win.bgcolor("lightgreen")
    spiral = turtle.Turtle()
    spiral.color("hotpink")
    sys.setExecutionLimit(35000)
    
    length = 5
    angle = 90   #change angle here to 90 or 88 degrees
    
    for i in range(100):
        draw_spiral(spiral, angle, length)
        length = length + 3
       
    win.exitonclick()
    
if __name__ == "__main__":   
    main()    

—

import turtle, sys

def draw_spiral(t, angle, length):
        t.right(angle)
        t.forward(length)
        
def main():
    win = turtle.Screen()
    win.bgcolor("lightgreen")
    spiral = turtle.Turtle()
    spiral.color("hotpink")
    sys.setExecutionLimit(35000)
    
    length = 5
    angle = 88
    
    for i in range(100):
        draw_spiral(spiral, angle, length)
        length = length + 3
       
    win.exitonclick()
    
if __name__ == "__main__":   
    main()    

—

import turtle, sys

sys.setExecutionLimit(35000)

def draw_spiral(t, angle):
    length = 1
    for i in range(100):
        t.right(angle)
        t.forward(length)
        length = length + 3
        
def main():
    win = turtle.Screen()
    win.bgcolor("lightgreen")
    spiral = turtle.Turtle()
    spiral.color("blue")
    spiral.speed(0)
    
    draw_spiral(spiral, 90)
    spiral.goto(0, 0)
    draw_spiral(spiral, 88)
           
    win.exitonclick()
    
if __name__ == "__main__":   
    main()    

—

import turtle

def draw_equi_triangle(t, sides, side_length, angle):
    for i in range(1):
        draw_poly(t, sides, side_length, angle)


def draw_poly(t, sides, side_length, angle):
    for i in range(sides):
        t.forward(side_length)
        t.left(angle)


def main():
    win = turtle.Screen()
    skippy = turtle.Turtle()
    skippy.speed(8)
    
    sides = int(input("How many sides does an equilateral triangle have? (trick question)"))
    side_length = int(input("How long would you like the sides of your triangle to be?"))
    angle = (360/sides)
    draw_equi_triangle(skippy, sides, side_length, angle)
    
    
main()
    

—

def sum_to(n):
    result = (n * (n + 1)/2)
    return result

print(sum_to(10))

—

import turtle

def draw_star(t):
    for i in range(5):
        t.left(144)
        t.forward(100)
        
def main():
    win = turtle.Screen() 
    star = turtle.Turtle() 
    draw_star(star)

    win.exitonclick()
    
    
if __name__ == "__main__":
    main()  

—

import turtle

def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.left(144)
        
def main():
    win = turtle.Screen()
    win.setup(700, 700)
    win.bgcolor("lightgreen")
    star = turtle.Turtle()
    star.color("HotPink")
    star.penup()
    star.goto(-200, 0)
    star.pendown()
    star.speed(10)
    star.pensize(3)
    
    for i in range(5):           #pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star
        draw_star(star)
        star.penup()
        star.forward(350)
        star.left(144)
        star.pendown()
         

    win.exitonclick()
    
    
if __name__ == "__main__":
    main()  

—

import turtle

def draw_star(t, n):
    for i in range(n):
        t.forward(100)
        t.left(180-180/n)

def main():
    star = turtle.Turtle()
    star.speed(10)
    draw_star(star, 11)

if __name__ == "__main__":
    main()

—

import turtle

def draw_sprite(t, legs, leg_length):
    for i in range(legs):
        t.forward(leg_length)
        t.backward(leg_length)
        t.right(360/legs)

def main():
    win = turtle.Screen()
    sprite = turtle.Turtle()
    
    num_legs = int(input("Number of legs?"))
    length_legs = int(input("Length of legs?"))
    
    
    draw_sprite(sprite, num_legs, length_legs)
    
    
    
if __name__ == "__main__":
    main()
    
—

def sum_to(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum

def main():
    sum = sum_to(8)
    print("The sum of all integers up to and including n is", sum)

if __name__ == "__main__":
    main()
—

import turtle

def draw_sprite(t, legs, leg_length):
    for i in range(legs):
        t.forward(leg_length)
        t.backward(leg_length)
        t.right(360/legs)
    
        
def fancy_square(t, legs, leg_length, sq_size):
    for i in range(4):
        t.forward(sq_size)
        t.right(90)
        draw_sprite(t, legs, leg_length)
        
        
def main():
    win = turtle.Screen()
    sprite = turtle.Turtle()
    sprite.speed(10)
    
    legs = int(input("Number of legs?"))
    leg_length = int(input("Length of legs?"))
    sq_size = int(input("How long are the sides of the square?"))
    
    fancy_square(sprite, legs, leg_length, sq_size)
    
    win.exitonclick()
    
if __name__ == "__main__":
    main()

—

import math

def area_of_circle(r):
    area = math.pi*(r**2)
    return area

—

import turtle

def draw_shape(t, n):
    
     for i in range(4):   
        for i in range(4):
            t.forward(n)
            t.right(90)
        t.left(90)
        t.right(360/5)
    
    
def main():
    win = turtle.Screen()
    win.setup(700, 700)
    win.bgcolor("lightgreen")
    boxy = turtle.Turtle()
    boxy.color("blue")
    boxy.speed(0)
    
    n=200
    for i in range(5):
        draw_shape(boxy, n)

main()

—

def exponential(base, exp):
    accumulator = 1        # initialize the accumulator!
    for counter in range(exp):
         accumulator = accumulator*base

    return accumulator

print(exponential(10,2))


__

def fib(n):                  #fib(n)=fib(n-1)+fib(n-2), #fib(x)=fib(y)+fib(z)
    if n == 0:
        print(0)
    else:
        x = 0
        y = 1
        for i in range(1,n):
            z = (x + y)
            x = y
            y = z
        return y
        
    
n = 4

result = fib(n)
print(result)

—

def fib(n):                  #fib(n)=fib(n-1)+fib(n-2), but can't compute fib(0) or fib(1)
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
    
n = 4

result = fib(n)
print(result)

—
DOUG SOLUTION TO FIBONACCI

def fib(n):

	if n == 0:
		return 0
	if n == 1:
		return 1 
	total = 0		#variable to hold sum
	prev1 = 1
	prev2 = 0
	#loop
	for i in range(n-1):
	#add stuff to variable
		total = prev1 + prev2
		prev2 = prev1
		prev1 = total
	return total

print(fib(4))
#answer 3
—



BEGIN CHAPTER 6

—

def grade(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "A"
    elif x >= 70:
        return "A"
    elif x >= 60:
        return "A"
    else:
        return "F"
               
def main():       
    score = 39.99999
    grade(score)
    print("If your score is", str(score), "your grade is", grade(score))


if __name__ == "__main__":
    main()
—

import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape
    
def fillcolor(t, data):
    for x in range(data, data+1):
        if x >= 200:
            t.fillcolor("red")
        else:
            if 100 < x < 200:
                t.fillcolor("yellow")
            else:
                t.fillcolor("green")

def main():
    data = [48, 117, 200, 240, 160, 260, 220]
    max_height = max(data)
    num_bars = len(data)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, 0-border, 40 * num_bars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.pensize(3)
    tess.speed(7)

    for x in data:
        fillcolor(tess, x)
        draw_bar(tess, x)

    wn.exitonclick()

if __name__ == "__main__":
    main()

—

import turtle				#can handle negative numbers

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    if height < 0:
        t.write(str(height))
    t.left(90)
    t.forward(height)
    if height > 0:
        t.write(str(height)) 
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape
    
def fillcolor(t, data):
    for x in range(data, data+1):
        if x >= 200:
            t.fillcolor("red")
        else:
            if 100 < x < 200:
                t.fillcolor("yellow")
            else:
                t.fillcolor("green")

def main():
    data = [48, 117, 200, -240, 160, 260, 220]
    max_height = max(data)
    num_bars = len(data)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, 0-border, 40 * num_bars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.pensize(3)
    tess.speed(7)

    for x in data:
        fillcolor(tess, x)
        draw_bar(tess, x)

    wn.exitonclick()

if __name__ == "__main__":
    main()

—

from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
testEqual(is_even(10), True)
testEqual(is_even(5), False)
testEqual(is_even(1), False)
testEqual(is_even(0), True)

—

from test import testEqual

def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)

—

from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    if is_even(n):
        return False
    else:
        return True

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)

—

def pick_activity(temp, moisture):
    if temp == "hot" and moisture == "wet":
        message = "Watch Netflix"
    elif temp == "hot" and moisture == "dry":
        message = "Go swimming!"
    elif temp == "cold" and moisture == "wet":
        message = "Paint"
    elif temp == "cold" and moisture == "dry":
        message = "Go to a cafe and read."
    else:
        message = "Invalid input"
    return message

    
print(pick_activity("cold", "dry"))

—

from test import testEqual

def is_rightangled(a, b, c):
    result = a**2 + b**2
        
    if abs(c**2 - result) < 0.001:
        return True
    else:
        return False
    
    
    # your code here

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)

—
from test import testEqual
    
def is_rightangled(a, b, c):
    rightangled = False

    if a > b and a > c:		#I also did this with max(a, b, c) but lost it :(
        rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c:
        rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        rightangled = abs(a**2 + b**2 - c**2) < 0.001
    return rightangled
    
    
    


testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(16.0, 4.0, 8.0), False)
testEqual(is_rightangled(4.1, 9.1678787077, 8.2), True)
testEqual(is_rightangled(9.16787, 4.1, 8.2), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.64031, 0.4), True)
—

def date_of_easter(year):
    # Your code here
    if year >= 1900 and year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        date = 22 + d + e
        
       
        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            date = (date - 7)

        if date > 31:
                return("Easter is on April " + str(date - 31))
        else:
            return("Easter is on March " + str(date))
        
        
    
    if year <=1900 or year >= 2099:
        print("Invalid input.")
    

def main():
    # Your code here
    year_x = int(input("Enter a year from 1900 to 2099."))
    print(date_of_easter(year_x))
    
                 
if __name__ == "__main__":
    main()
—

def pos_or_neg(num):
    if num > 0:
        print('positive')
    elif num < 0:
        print('negative')


def print_positives(the_ints):
    for num in the_ints:
        if num > 0:
            print(num)


def print_signed_integers(the_ints, the_sign):
    if the_sign == 'positive':
        for i in the_ints:
            if i > 0:
                print(i)
    elif the_sign == 'negative':
        for i in the_ints:
            if i < 0:
                print(i)
int = -3
ints = [3, 4, -1, -5]  
sign = "positive"
pos_or_neg(int)
print_positives(ints)
print_signed_integers(ints, sign)

—

def sherlock(guests):
    for guest in guests:
        if guest == "Dr. Watson" or guest == "Inspector Lestrade":
            return "Enter"
        else:
            return "Go Away! (sound of violin music...)"

def main():
    press = ["a reporter from the Times", "a reporter from the Observer"]
    family_etc = ["Mycroft Holmes", "Mrs. Hudson"]
    enemies = ["Professor Moriarty", "Charles Augustus Milverton", "John Woodley"]
    potential_love_interest = ["Irene Adler"]
    friends = ["Inspector Lestrade", "Dr. Watson"]
    print(sherlock(press))
    print(sherlock(family_etc))
    print(sherlock(enemies))
    print(sherlock(potential_love_interest))
    print(sherlock(friends))

if __name__ == "__main__":
    main()

—
def some_function():
    # Imagine code that could raise value or unicode errors
    pass

def main():
    # Put your exception handling code below
    try:
        some_function()
    except UnicodeError:
        print("Unicode error happening now.")
    except ValueError:
        print("Value error happening now.")

if __name__ == "__main__":
    main()
—

def line(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + "#"
        
    return line_str

def main():
    n = 5
    print(line(n))
    
if __name__ == "__main__":
    main()

—

def line(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + "#"
        
    return line_str

def square(n):
    square_str = ''
    for i in range(n):
        square_str = square_str + (line(n) + '\n')   #'\n' is newline
    return square_str

def main():
    n = 10
    print(square(n))
    
if __name__ == "__main__":
    main()
—

def line(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + "#"
        
    return line_str

def rectangle(n, p):
    rectangle_str = ''
    for i in range(p):
        rectangle_str = rectangle_str + (line(n) + '\n')   #'\n' is newline
    return rectangle_str

def main():
    n = 5
    p = 3
    print(rectangle(n, p))
    
if __name__ == "__main__":
    main()

—

def line(n):
    line_str = ''
    for i in range(n):
        line_str = line_str + "#"
        
    return line_str

def stairs(n):
    stair_str = ''
    for level_len in range(n):
        stair_str += (line(level_len+1) + '\n')

    return stair_str

def main():
    n = 5
    print(stairs(n))
    
if __name__ == "__main__":
    main()

—

from test import testEqual

def insert(sorted_list, num):
    
    #Doug's code
    #make index
    index = 0
    
    #find the spot where the number goes (element from list is greater than num)
    while index < len(sorted_list) and sorted_list[index] < num:
        index = index + 1

    #first part of the list before index gets copied
    result = sorted_list[:index]
    
    #insert the number
    result.append(num)
    
    #tack on the end of the list (concatonation)
    result = result + sorted_list[index:]
    
    return result
        
    #original solution
    #new_idx = 0

    #while new_idx < len(sorted_list) and num > sorted_list[new_idx]:
        #new_idx += 1

    #new_sorted_list = sorted_list[:new_idx]
    #new_sorted_list.append(num)

    #for item in sorted_list[new_idx:]:
        #new_sorted_list.append(item)

    #return new_sorted_list


testEqual(insert([2,3], 1), [1,2,3])
testEqual(insert([1,3], 2), [1,2,3])
testEqual(insert([1,2], 3), [1,2,3])

—

# Sorts a list using bubble sort. Can use list.sort
def bubble_sort(alist):
    # TODO your code here
    is_sorted = False
    while is_sorted == False:
        num_swaps = 0
        for a in range(len(alist) - 1):
            if alist[a] > alist[a + 1]:
                temp = alist[a]
                alist[a] = alist[a + 1]
                alist[a + 1] = temp
                
                num_swaps = num_swaps + 1
                
        if num_swaps == 0:
            is_sorted = True
    return alist


from test import testEqual
testEqual(bubble_sort([0]), [0])  # Sorts a single element, returns same list
testEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Sorted list is the same
testEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
testEqual(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
—

def print_triangular_numbers(n):
    i = 0
    
    for i in range(1, n + 1):
        i = (i*(i+1))//2
        print(i)
        

print_triangular_numbers(8)

—

import random
import turtle


def is_in_screen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False


def main():
    julia = turtle.Turtle()
    screen = turtle.Screen()

    julia.shape('turtle')
    while is_in_screen(screen, julia):

        # simulates a coin flip (0 is heads, 1 is tails)
        coin = random.randrange(0, 2)
        angle = random.randrange(0, 361)

        if coin == 0:
            julia.left(angle)
        else:
            julia.right(angle)

        julia.forward(50)

    screen.exitonclick()

if __name__ == "__main__":
    main()

—

import random
import turtle

def move_random(screen, t):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)
    
def are_colliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

def is_in_screen(screen, t):
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in

def main():
    julia = turtle.Turtle()
    frank = turtle.Turtle()
    screen = turtle.Screen()

    julia.shape('turtle')
    frank.shape('square')
    
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2
    
    julia.up()
    julia.goto(random.randrange(left_bound, right_bound),
            random.randrange(bottom_bound, top_bound))
    julia.setheading(random.randrange(0, 360))
    julia.down()

    frank.up()
    frank.goto(random.randrange(left_bound, right_bound),
            random.randrange(bottom_bound, top_bound))
    frank.setheading(random.randrange(0, 360))
    frank.down()
        
    while is_in_screen(screen, julia) and is_in_screen(screen, frank):
        move_random(screen, julia)
        move_random(screen, frank)


    screen.exitonclick()

if __name__ == "__main__":
    main()

—

def course_grader(test_scores):
    # Your code here
    grade = sum(test_scores)/len(test_scores)
    while grade >= 70 and min(test_scores) > 50:
        return "pass"
    else:
        return "fail"
    return grade

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()
—

	a.	‘Python’[1] = ‘y’
	b.	‘Strings are sequences of characters.’[5] = ‘g’
	c.	len(‘wonderful’) = 9
	d.	‘Mystery’[:4] = ‘Myst’
	e.	‘p’ in ‘Pineapple’ = True
	f.	‘apple’ in ‘Pineapple’ = True
	g.	‘pear’ not in ‘Pineapple’ = True
	h.	‘apple’ > ‘pineapple’ = False
	i.	‘pineapple’ < ‘Peach’ = False


—

def digits(n):
    length = str(n)
    return len(length)
  
print(digits(543))

—

from test import testEqual

def remove(substr, originalstr):
    # your code here
    index = originalstr.find(substr)
    if index < 0: # substr doesn't exist in original_string
        return originalstr
    return_str = originalstr[:index] + originalstr[index+len(substr):]
    return return_str
        

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
testEqual(remove('oo', 'Yahoohoo'), 'Yahhoo')

—

from test import testEqual

def reverse(text):
    word = str(text)
    back = ''
    for item in word:
        back = item + back
    return back
    
  

testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""), "")

—

from test import testEqual

def reverse(text):
    word = str(text)
    back = ''
    for item in word:
        back = item + back
    return back
    
def is_palindrome(text):
    # your code here
    word = str(text)
    is_palindrome == False
    if word == reverse(text):
        return True
    else:
        return False

testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)

—

def mirror(text):
    # your code 
    word = str(text)
    return word + reverse(text)

def reverse(text):
    # your code here
    word = str(text)
    back = ''
    for item in word:
        back = item + back
    return back


from test import testEqual
testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')

—

def analyze_text(text):
    
    text_str = str(text)
 
    
    total_e = text_str.count("e") + text_str.count("E")
    total_alpha = sum(c.isalpha() for c in text_str)
    percent_e = (total_e/total_alpha)*100
    #return(total_e, total_alpha, percent_e)
    answer = "The text contains " + str(total_alpha) + " alphabetic characters, of which "+ str(total_e) + " ("+str(percent_e)+"%) are 'e'."
    return answer
    —

def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    names_list = fullname.split()
    
    print(names_list)

    #first = letters_list[0][0]
    #last = letters_list[1][0]
    
    #initials = first.upper() + last.upper()
    #return initials
    
    inits = ''
    for names in names_list:
        inits = names[0].upper() + inits
    return inits
    print()


name = "bonnie"
inits = get_initials(name)
print("The initials of", name, "are", inits)
# => prints "The initials of 'Ozzie Smith' are OS"
 —

from test import testEqual

# (Doug code)
def average_sales(daily_sales):
    
    #how many weeks do we have?
    weeks = len(daily_sales)
    result = []
    
    #for each week's data
    for i in range(weeks):      #or for week in daily_sales
    
        #add up data from the days, accumulator pattern
        weekly_sum = 0
        
        for day in daily_sales[i]:     #or for day in week
            weekly_sum = weekly_sum + day  #or weekly_sum += day
        
        #divide by number of days to get average
        weekly_avg = weekly_sum / len(daily_sales[i])   #or len/(week)
    
        
        #add computed average to the list
        result.append(weekly_avg)
        
    return result



#(original code follows)
#def average_sales(daily_sales):

    #num_weeks = len(daily_sales)
    #weekly_averages = [0 for i in range(num_weeks)]

    #for week in range(0, num_weeks):

        # calculate the average for the given week
        #week_sum = 0
        #for day_total in daily_sales[week]:
            #week_sum += day_total

        #weekly_averages[week] = week_sum / len(daily_sales[week])

    #return weekly_averages


sales = [[1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 0, 2, 1, 1]]

testEqual(average_sales(sales), [1, 1])

—

import random
from test import testEqual

# The roll_dice function simulates the rolling of the dice. It
# creates a 2 dimensional list: each column is a die and each
# row is a throw. The function generates random numbers 1-6
# and puts them in the list.
def roll_dice(num_dice, num_rolls):

    # create a two-dimensional (num_dice by num_rolls) of zeros
    double_list = [[0 for i in range(num_dice)] for j in range(num_rolls)]

    # loop through each row and column, filling it with a random roll
    for roll in range(0, len(double_list)):
      for die in range(0, len(double_list[roll])):
          double_list[roll][die] = (int)(random.random()*6 + 1)

    return double_list


# This function takes a 2D list (which can be generated by roll_dice)
# and sums the value of all the dice in each row. It returns a 1
# dimensional list with the sum of each throw.
# Example:
# double_list: [[1, 5, 6],[2, 3, 1],[1, 3, 3]]
# sum_of_roll should return: [12, 6, 7]



def sum_of_roll(double_list):
    # Your code here
    list = len(double_list)
    roll_sum = []
    
    for turn in range(list):
        sum = 0
        for roll in double_list[turn]:
            sum = sum + roll
            
        roll_sum.append(sum)
        
    return roll_sum

# Bonus function! Takes a 2D list and returns
# the number of times a person rolls Yahtzee (all dice have
# the same value). Hint: you may want to create a helper
# function that takes individual rows of the list.
def yahtzee(double_list):
    # Bonus: your code here
    counter = 0
    for i in range(len(double_list)):
        if one_yahtzee(double_list[i]) == True:
            counter = counter +1
        
        
    return counter
    
    
def one_yahtzee(list):     #checks one roll
    first = list[0]
    for die in list:
        if die != first:
            return False
    return True

#(Melissa Code)    
#def yahtzee(double_list):
    # Bonus: your code here
        
    #list = len(double_list)
    
    #for turn in range(list):
        #sum = 0
        #for roll in double_list[turn]:
            #while roll[0] == roll[1] and roll[1] == roll[2]:
                #return True
            #else:
                #return False


# To play, yo'd do something like this
# dice = input("How many dice?")
# rolls = input("What is the number of rolls?")
# list = roll_dice(dice, rolls)
# print("Sum of roll:", sum_of_roll(list))

print("Testing sum_of_roll...")
testEqual(sum_of_roll([[4, 5, 2],[6,2,1],[4,4,4]]), [11, 9, 12])
testEqual(sum_of_roll([[3, 4, 6],[2,6,1],[3,4,3]]), [13, 9, 10])
print("Testing yahtzee...")
testEqual(yahtzee([[4, 5, 2],[6,2,1],[4,4,4]]), 1)
testEqual(yahtzee([[3, 4, 6],[2,6,1],[3,4,3]]), 0)
—
my_list = []

my_list.append(76)
my_list.append(92.3)
my_list.append("hello")
my_list.append(True)
my_list.append(4)
my_list.append(76)
   
print(my_list)

my_list = [76] + [92.3] + ["hello"] + [True] + [4] + [76]
print(my_list)

__

my_list = [76, 92.3, 'hello', True, 4, 76]
my_list.append("apple")       #Append “apple” and 76 to the list.
my_list.append(76)
print(my_list)
(my_list.insert(3,"cat"))     #insert the value “cat” at position 3.
print(my_list)
(my_list.insert(0, 99))       #insert the value 99 at the start of the list.

print(my_list)
print(my_list.index("hello"))     #Find the index of “hello”.
print(my_list.count(76))          #Count the number of 76s in the list.
print(my_list.pop(1))             #Remove the first occurrence of 76 from the list.
print(my_list.index(True))        #Remove True from the list using pop and index.
my_list.pop(4)                         #or combine into my_list.pop(my_list.index(True))

print(my_list)

—

def odds(numbers):
    num_odds = 0
    
    for num in numbers:
        if num % 2 != 0:
            num_odds = num_odds + 1
        
    return num_odds

def main():

    list = [3,5,8,9,2]
    odds(list)
    print(odds(list))
    
if __name__ == "__main__":
    main()

—

import random

def max(numbers):
    max = 0
    for num in numbers:
        if num > max:
            max = num
    return max
    
    
def main():
    list = []
    for i in range(100):
        list.append(random.randint(1, 1000))
    #print(list)
    max(list)
    print(max(list))

if __name__ == "__main__":
    main()

—

def sum_of_squares(xs):
    sum = 0
    for num in xs:
        sum = num**2 + sum
    return sum
    
    
    
xs = [2, 3, 4]
sum_of_squares(xs)
print(sum_of_squares(xs))

—

def sum_negs(list):
    sum = 0
    for num in list:  
        if num < 0:
            sum = sum + num
    return sum
    

list = [-2, -7, 4, 0, -1]
sum_negs(list)
print(sum_negs(list))

—

def count(list):
    sum = 0
    for word in list:
        if len(word) == 5:
            sum = sum + 1
    return sum

list = ["this", "is", "a", "list", "of", "words", "of", "several", "small", "lengths", "uitor"]
count(list)
print(count(list))
—

def count(obj, list):
    sum = 0
    for item in list:
        if item == obj:
            sum = sum + 1
    return sum

def is_in(obj, list):
    for item in list:
        if item == obj:
            return True
        return False     
        
def rev(list):
    reverse = []
    for item in range(len(list)-1, -1, -1): # step through the original list backwards
        reverse.append(list[item])
    return reverse

def indexy(obj, list):
    for item in range(len(list)):
        if list[item] == obj:
            return item
    return -1

def insert(obj, index, list):
    new_list = []
    for item in range(len(list)):
        if item == index:
            new_list.append(obj)
        new_list.append(list[item])
    return new_list
        

obj = 5
index = 2
list = [1, 2, 3, 4, 5]
print(count(obj, list))
print(is_in(obj, list))
print(rev(list))
print(indexy(obj, list))
print(insert("puppy", index, list))

—

#def replace(s, old, new):
    #wds = s.split(old)
    #glue = new
    #new = glue.join(wds)
    #return new


def replace(s, old, new):
    new_list = s.split(old)
    new_list2 = new.join(new_list)
    return new_list2
    
    
    
    
s = "Mississippi"
old = "i"
new = "I"
print(replace(s, old, new))
    
—

def sum_of_initial_odds(nums):
    # your code here
    sum = 0
    for num in nums:
        if num % 2 != 0:
            sum = sum + num
        else:
            break
    return sum


from test import testEqual

testEqual(sum_of_initial_odds([1,3,1,4,3,8]), 5)
testEqual(sum_of_initial_odds([6,1,3,5,7]), 0)
testEqual(sum_of_initial_odds([1, -7, 10, 23]), -6)
testEqual(sum_of_initial_odds(range(1,555,2)), 76729)

—

def get_country_codes(prices):
    # your code here
    
    #print(prices)
    new_list = prices.split()
    #print(new_list)
    
    country_codes = []
    for price in new_list:
        #country_codes = country_codes + price[0] + price[1]
        country_codes.append(price.strip()[0:2])
    return ', '.join(country_codes)  


    
# don't include these tests in Vocareum
from test import testEqual

testEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
testEqual(get_country_codes("CA$40"), "CA")
—

x = input("Please enter a sentence.")

x = x.lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_count = {}
for char in x:
    if char in alphabet:
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = letter_count.keys()
keys.sort()
for char in keys:
    print(char, letter_count[char])

—

def get_count(test_string):
    letter_count = {}
    for letter in test_string:                              
        if letter in letter_count:                                    #or 'if dictionary.get(i, False):', or 'if letter in dictionary.keys:'
            letter_count[letter] = letter_count[letter] + 1
        else:
            letter_count[letter] = 1
    
    keys = sorted(letter_count.keys())
    #keys.sort()
    for letter in keys:
        print(letter, letter_count[letter])
        

def main(): 
    test_string = input("Enter a sentence and the characters will be counted.")
    print(get_count(test_string))

if __name__ == '__main__':
    main()

—

def main():

    students = {}

    # Use a space to allow for the while check below
    new_student = " "

    # Get student names
    while (new_student != ""):
        new_student = input("Student's name (or press ENTER to finish)")
        if new_student != "":
            new_grade = float(input("Grade for " + new_student + ": "))
            students[new_student] = new_grade
    
    #prin to check roster
    print(students)   
    
    # Print class roster
    print("\nClass roster:")       
    for x in students.keys():
        print(x + " (" + str(students[x]) + ")")
    
    avg = sum(students.values()) / len(students)
    print("\nAverage grade: " + str(avg))
   
if __name__ == '__main__':
    main()
—

def clock_in(worker_dict, worker, time_in):
    worker_info = worker_dict.get(worker)
    worker_info[0] = time_in
    worker_dict[worker] = worker_info

    
    
def clock_out(worker_dict, worker, time_out):
    worker_info = worker_dict.get(worker)
    worker_info[1] = time_out
    worker_info[2] = worker_info[1] - worker_info[0]
    worker_dict[worker] = worker_info




def main():
    workers = {"George Spelvin": [0,0,0], "Jane Doe": [0,0,0], "John Smith": [0,0,0]}
    print(workers.get("George Spelvin"))   # should print [0,0,0]
    clock_in(workers, "George Spelvin", 8)
    clock_out(workers, "George Spelvin", 17)
    print(workers.get("George Spelvin"))   # should print [8, 17, 9]


    
if __name__ == "__main__":
    main()
—

from test import testEqual

def translate(text):
# your code here!
    pirate_dict = {'sir':'matey',"hotel":"fleabag inn","student":"swabbie","boy":"matey","madam":"proud beauty","professor":'foul blaggart',"restaurant":"galley","your":"yer","excuse":"arr","students":"swabbies","are":"be","lawyer":'foul blaggart',"restroom":"th’ head","my":"me","hello":"avast","is":"be","man":'matey'}
    pirate_speak=''
    word_list = text.split()
    for word in word_list:
        if word in pirate_dict:
            word = pirate_dict[word]
        pirate_speak = pirate_speak+' '+ word
    return pirate_speak

def main():
    eng_speak = input("Give me a sentence and I'll translate it to Pirate, Matey!")
    print(translate(eng_speak))
    


text = "hello my man, please excuse your professor to the restroom!"
testEqual(translate(text), "avast me matey, please arr yer foul blaggart to th' head!")

—

from test import testEqual

pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['madam'] = 'proud beauty'
pirate['professor'] = 'foul blaggart'
pirate['restaurant'] = 'galley'
pirate['your'] = 'yer'
pirate['excuse'] = 'arr'
pirate['students'] = 'swabbies'
pirate['are'] = 'be'
pirate['lawyer'] = 'foul blaggart'
pirate['restroom'] = "th' head"
pirate['my'] = 'me'
pirate['hello'] = 'avast'
pirate['is'] = 'be'
pirate['man'] = 'matey'

def translate(text):
# your code here!        
        
    #print(pirate)
    pirate_speak =''
    word_list = text.split()
    print(word_list)
    for word in word_list:
        if word in pirate:
            word = pirate[word]
        pirate_speak = pirate_speak +' '+ word
    return pirate_speak

def main():
    eng_speak = input("Give me a sentence and I'll translate it to Pirate, Matey!")
    print(translate(eng_speak))
    


text = "hello my man, please excuse your professor to the restroom!"
testEqual(translate(text), "avast me matey, please arr yer foul blaggart to th' head!")

—

from test import testEqual

def translate(text):
    pirate = {}
    pirate['sir'] = 'matey'
    pirate['hotel'] = 'fleabag inn'
    pirate['student'] = 'swabbie'
    pirate['boy'] = 'matey'
    pirate['madam'] = 'proud beauty'
    pirate['professor'] = 'foul blaggart'
    pirate['restaurant'] = 'galley'
    pirate['your'] = 'yer'
    pirate['excuse'] = 'arr'
    pirate['students'] = 'swabbies'
    pirate['are'] = 'be'
    pirate['lawyer'] = 'foul blaggart'
    pirate['restroom'] = "th' head"
    pirate['my'] = 'me'
    pirate['hello'] = 'avast'
    pirate['is'] = 'be'
    pirate['man'] = 'matey'

    print(pirate)
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    no_punct = ""
    for char in text:
        if char not in punctuations:
            no_punct = no_punct + char


    print(no_punct)

    pirate_sentence = []
    word_list = no_punct.split()
    for word in word_list:
        if word in pirate:
            pirate_sentence.append(pirate[word])
        else:
            pirate_sentence.append(word)
    
    
    return((" ").join(pirate_sentence))


text = "hello my man, please excuse your professor to the restroom!"
testEqual(translate(text), "avast me matey, please arr yer foul blaggart to th' head!")

—

# Create sort_contacts function
def sort_contacts(contacts):
    #contacts = {}
    #list(contacts)
    #return list(sorted(contacts.items())) #produces nested tuple
    
    return sorted((k,)+v for k, v in contacts.items())

# The code below is just for your testing purposes. Make sure you pass all the tests.
# In Vocareum, only put code for the sort_contacts function above
from test import testEqual

testEqual(sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}), [('Freud, Anna', '1-541-754-3010',
        'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
        ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')])
testEqual(sort_contacts({"Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
    "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")}),
    [('Rudolph, Wilma', '1-410-5313-584', 'wilma@olympians.com'),
    ('Summitt, Pat', '1-865-355-4320', 'pat@greatcoaches.com')])
testEqual(sort_contacts({"Dinesen, Isak": ("1-718-939-2548", "isak@storytellers.com")}),
    [('Dinesen, Isak', '1-718-939-2548', 'isak@storytellers.com')])
testEqual(sort_contacts({"Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
    "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
    "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"), "Kandinsky, Wassily":
    ("1-333-555-9999", "kandinsky@painters.com")}), [('Almodovar, Pedro', '1-990-622-3892',
    'pedro@filmbuffs.com'), ('Kandinsky, Wassily', '1-333-555-9999', 'kandinsky@painters.com'),
    ('Rimbaud, Arthur', '1-636-555-5555', 'arthur@notlive.com'), ('Swinton, Tilda',
    '1-917-222-2222', 'tilda@greatActors.com')])

—


alphabet = {'a':0, 'A':0, 'b':1, 'B':1, 'c':2, 'C':2, 'd':3, 'D':3, 'e':4, 'E':4, 'f':5, 'F':5, 'g':6, 'G':6, 'h':7, 'H':7, 'i':8, 'I':8, 'j':9, 'J':9, 'k':10, 'K':10, 'l':11, 'L':11, 'm':12, 'M':12, 'n':13, 'N':13, 'o':14, 'O':14, 'p':15, 'P':15, 'q':16, 'Q':16, 'r':17, 'R':17, 's':18, 'S':18, 't':19, 'T':19, 'u':20, 'U':20, 'v':21, 'V':21, 'w':22, 'W':22, 'x':23, 'X':23, 'y':24, 'Y':24, 'z':25, 'Z':25}



—

import math

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distance_from_point(self, target):
        dfx = (self.x - target.x)
        dfy = (self.y - target.y)
        return math.sqrt(dfx**2 + dfy**2)
               
    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

def main():
    p = Point(3, 3)
    q = Point(6, 7)
    print(p.distance_from_point(q))

if __name__ == "__main__":
    main()

—

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def reflect_x(self):
        neg_y = (0 - self.x)
        return "(" + str(self.x) +", "+ str(neg_y) + ")"

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
def main():
    p = Point(3, 3)
    q = Point(6, 7)
    print(p.reflect_x())

if __name__ == "__main__":
    main()

—

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    # TODO define a method called slope_from_origin here
    def slope_from_origin(self):
        y_diff = (self.y - 0)
        x_diff = (self.x - 0)
        if x_diff == 0:
            return None
        else:
            return (y_diff)/(x_diff)
        

    

# some tests to check your code
from test import testEqual
testEqual( Point(4, 10).slope_from_origin(), 2.5 )
testEqual( Point(5, 10).slope_from_origin(), 2 )
testEqual( Point(0, 10).slope_from_origin(), None )
testEqual( Point(20, 10).slope_from_origin(), 0.5 )
testEqual( Point(20, 20).slope_from_origin(), 1 )
testEqual( Point(4, -10).slope_from_origin(), -2.5 )
testEqual( Point(-4, -10).slope_from_origin(), 2.5 )
testEqual( Point(-6, 0).slope_from_origin(), 0 )

—

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    
def main():
    p = Point(3, 3)
    print(p.move(1,5))

if __name__ == "__main__":
    main()

—

# TODO: add the Car class
class Car:
    
    def __init__(self, gas_level):
        self.x = gas_level
        
    def add_gas(self, amt):
        self.x = self.x + amt
    
    def fill_up(self):
        if self.x < 13:
            return 13-self.x
        else:
            return 0
        

# some tests to check your code, Do Not Post These in Vocareum
from test import testEqual
testEqual( Car(10).fill_up(), 3 )
testEqual( Car(20).fill_up(), 0 )
testEqual( Car(5.5).fill_up(), 7.5 )
testEqual( Car(12.5).fill_up(), 0.5 )
testEqual( Car(13).fill_up(), 0 )

—

class Rectangle:
    
    def __init__(self, init_l, init_w):
        self.l = init_l
        self.w = init_w
    
    def get_l(self):
        return self.l
    
    def get_w(self):
        return self.w
        
    def area(self):
        rec_area = self.l*self.w
        return rec_area
    
    def perimeter(self):
        perim = 2*self.l + 2*self.w
        return perim
    
    def is_square(self):
        if self.l == self.w:
            return True
        else:
            return False
        
def main():
    rect = Rectangle(2,3)
    print(rect.is_square())
    print(rect.perimeter())
    print(rect.area())
    
    
    
if __name__ == "__main__":
    main()


—
class Cat:
    
    def __init__(self, name, amtOfHair, voice):
        self.name = name
        self.lives = 9        #constant, all cats start with 9 lives
        self.amtOfHair = amtOfHair
        self.voice = voice
        
    def meow(self):
        print(self.name + " says: " + self.voice)
        
    def shed(self, howMuch):
        if self.amtOfHair >= howMuch:
            self.amtOfHair = self.amtOfHair - howMuch
        
    def getAmtofHair(self):
        return self.amtOfHair

franklin = Cat("Franklin", 40000, "MEEEEOW!")
franklin.meow()
print(franklin.getAmtofHair())
franklin.shed(500)
print(franklin.getAmtofHair())
sally = Cat("Sally", 5959595, "mew")
sally.meow()

—

class Player:
    
    def __init__(self, name, number, hand): #EVERY value must be set
        self.name = name       #changes
        self.num = number
        self.hand = hand
        self.rbis = 0          #constant
        self.games = 0
        self.hits = 0
        self.runs = 0
        
    def game(self, runs, hits, rbis):
        self.hits = self.hits + hits
        self.runs = self.runs + runs
        self.rbis = self.rbis + rbis
        self.games = self.games + 1
    
    def __str__(self):
        return "Name "+ self.name + " hits: " + str(self.hits) + " games: " + str(self.games) + " runs: " + str(self.runs) + " rbis: " + str(self.rbis)

    
doug = Player("Doug Shook", 7, "right")
doug.game(0,1,2)
print(doug)


—

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_low = letter.lower()
    return alphabet.index(letter_low)

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.isalpha():
        num = alphabet_position(char)
        new_num = (num + rot) % 26
        new_char = alphabet[new_num]
        if char.isupper():
            return new_char.upper()
        else:
            return new_char
    else:
        return char

def encrypt(text, key):
    key_length = len(key)
    new_text = ''
    for char in range(len(text)):
        text_position = alphabet_position(text[char])
        key_position = alphabet_position(key[char % key_length])
        num_value = (text_position + key_position) % 26
        new_text += alphabet[num_value]
    return new_text
    
def main():
    text = input("Type a message to be encrypted:")
    key = input("Enter the key word:")
    print(encrypt(text,key))

if __name__ == "__main__":
    main()

—

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
class Rectangle:
    
    def __init__(self, init_p, init_w, init_h):
        self.location = init_p
        self.width = init_w
        self.height = init_h
        
    def __repr__(self):
        return "Rectangle with width "+str(self.width)+" and height "+str(self.height)+"."

def main():
    loc = Point(4, 5)
    r = Rectangle(loc, 6, 5)
    print(r)

if __name__ == "__main__":
    main()

—

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
class Rectangle:
    
    def __init__(self, init_p, init_w, init_h):
        self.location = init_p
        self.width = init_w
        self.height = init_h
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
        
    def __repr__(self):
        return "Rectangle with width "+str(self.width)+" and height "+str(self.height)+"."

def main():
    loc = Point(4, 5)
    r = Rectangle(loc, 6, 5)
    print(r)
    print(r.get_height())

if __name__ == "__main__":
    main()

—

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
class Rectangle:
    
    def __init__(self, init_p, init_w, init_h):
        self.location = init_p
        self.width = init_w
        self.height = init_h
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def area(self):
        return self.width*self.height
        
    def __repr__(self):
        return "Rectangle with width "+str(self.width)+" and height "+str(self.height)+"."

def main():
    loc = Point(4, 5)
    r = Rectangle(loc, 6, 5)
    print(r)
    print(r.get_height())

if __name__ == "__main__":
    main()
    
    
from test import testEqual
r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.area(), 50)

—

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
class Rectangle:
    
    def __init__(self, init_p, init_w, init_h):
        self.location = init_p
        self.width = init_w
        self.height = init_h
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return (2*self.width) + (2*self.height)
        
    def __repr__(self):
        return "Rectangle with width "+str(self.width)+" and height "+str(self.height)+"."

def main():
    loc = Point(4, 5)
    r = Rectangle(loc, 6, 5)
    print(r)
    print(r.get_height())

if __name__ == "__main__":
    main()
    
    
from test import testEqual
r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.area(), 50)

from test import testEqual
r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.perimeter(), 30)

—
class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
class Rectangle:
    
    def __init__(self, init_p, init_w, init_h):
        self.location = init_p
        self.width = init_w
        self.height = init_h
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return (2*self.width) + (2*self.height)
    
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp
        
        
        
    def __repr__(self):
        return "Rectangle with width "+str(self.width)+" and height "+str(self.height)+"."

def main():
    loc = Point(4, 5)
    r = Rectangle(loc, 6, 5)
    print(r)
    print(r.get_height())

if __name__ == "__main__":
    main()
    
    
from test import testEqual
r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.area(), 50)

from test import testEqual
r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.perimeter(), 30)

from test import testEqual
r = Rectangle(Point(100, 50), 10, 5)
testEqual(r.width, 10)
testEqual(r.height, 5)
r.transpose()
testEqual(r.width, 5)
testEqual(r.height, 10)


—

from test import testEqual

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
class Rectangle:
    
    def __init__(self, init_p, init_w, init_h):
        self.location = init_p
        self.width = init_w
        self.height = init_h
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return (2*self.width) + (2*self.height)
    
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp
        
    def contains(self, Point):
        x = Point.get_x()
        y = Point.get_y()
        return 0 <= x < self.width and 0 <= y < self.height
        
        
        
    def __repr__(self):
        return "Rectangle with width "+str(self.width)+" and height "+str(self.height)+"."

def main():
    loc = Point(4, 5)
    r = Rectangle(loc, 6, 5)
    
if __name__ == "__main__":
    main()
    
    



r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.contains(Point(0, 0)), True)
testEqual(r.contains(Point(3, 3)), True)
testEqual(r.contains(Point(3, 7)), False)
testEqual(r.contains(Point(3, 5)), False)
testEqual(r.contains(Point(3, 4.99999)), True)
testEqual(r.contains(Point(-3, -3)), False)

—

import math
from test import testEqual

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
class Rectangle:
    
    def __init__(self, init_p, init_w, init_h):
        self.location = init_p
        self.width = init_w
        self.height = init_h
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return (2*self.width) + (2*self.height)
    
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp
        
    def contains(self, Point):
        x = Point.get_x()
        y = Point.get_y()
        return 0 <= x < self.width and 0 <= y < self.height
    
    def diagonal(self):
        diag = math.sqrt(self.width**2+self.height**2)
        return diag
        
        
        
    def __repr__(self):
        return "Rectangle with width "+str(self.width)+" and height "+str(self.height)+"."

def main():
    loc = Point(4, 5)
    r = Rectangle(loc, 6, 5)
    
if __name__ == "__main__":
    main()
    
    



r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.contains(Point(0, 0)), True)
testEqual(r.contains(Point(3, 3)), True)
testEqual(r.contains(Point(3, 7)), False)
testEqual(r.contains(Point(3, 5)), False)
testEqual(r.contains(Point(3, 4.99999)), True)
testEqual(r.contains(Point(-3, -3)), False)

from test import testEqual
r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.diagonal(), 11.1803398875)

r1 = Rectangle(Point(0,0), 12, 4)
testEqual(r1.diagonal(), 12.6491106407)

r2 = Rectangle(Point(0,0), 1,2)
testEqual(r2.diagonal(), 2.2360679775)

—

class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"
    
class BoredChatbot(Chatbot):
    
    
    def response(self, human_message):
        if len(human_message) > 20:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return Chatbot.response(self, human_message)


# make a chatbot
sally = BoredChatbot("Sally")
# introduce the chatbot and allow the user to say something
human_message = input(sally.greeting())
# respond to the user
print(sally.response(human_message))

—

class Post:
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0

    def like(self):
        self.likes += 1     #mutator method!!! Manipulates one of the instance vars

    def __str__(self):
        return self.title + " by " + self.author


class VideoPost(Post):
    def __init__(self, title, author, url):
        Post.__init__(self, title, author, None)
        self.video_url = url
        self.plays = 0

    def play(self):
        self.plays += 1

    def __str__(self):
        return self.title + " played " + str(self.plays) + " times"
        #return Post.__str__(self) + " Plays: " + str(self.plays)

class LinkPost(Post):
    
    def __init__(self, title, author, url):
        Post.__init__(self, title, author, None)
        self.link_url = url
        self.clicks = 0
        
    def click(self):
        self.clicks += 1
                
    def __str__(self):
        return self.title + ": " + self.link_url
    
class ImagePost(Post):
    
    def __init__(self, title, author, file_name):
        Post.__init__(self, title, author, None)
        self.file_name = file_name
        
        return self.title + " by " + self.author

plain_post = Post("10 Best Albums of 2016", "Chris Bay", "1. Little Scream - Cult Following 2. ...")
vid_post = VideoPost("Little Scream - Love As a Weapon", "Chris Bay", "https://youtu.be/Tq4Vw4MB6eA")
pic_post = ImagePost("Cats in space", "Crystal Martin", "spacecats.gif")
url_post = LinkPost("LaunchCode's LC101", "LaunchCode Staff", "https://www.launchcode.org/lc101")

vid_post.play()
vid_post.play()
url_post.click()

print(vid_post)
print(plain_post)
print(url_post)
print(pic_post)

—


