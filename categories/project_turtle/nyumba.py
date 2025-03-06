"""
Project: Kasa (Just a heads up Nyumba means house in Swahili)
Author Babu Macharia

The Purpose of this program is to draw a house using the turtle module

"""

import turtle as t


# A square has 4 equal sides and 4 equal angles
def square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)


# A rectangel has 4 sides with the opposite sides being equal
def rectangle(length, width):
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)


# An equilateral triangle has 3 equal sides and 3 equal angles 0f 120 degrees
def triangle(length):
    for i in range(3):
        t.forward(length)
        t.left(120)

def house(len): 
    square(len)
    triangle(len)  
    


def main():
  t.speed(0)
  t.color("green")
  t.pensize(3)
  house(100)
  t.color("blue")
  t.penup()
  t.forward(200)
  t.pendown()
  house(50)  
  
  

if __name__ == "__main__":
  main()
  t.Screen().exitonclick()
  