"""
Name: Babu Macharia
Project: Stop Sign

The Purpose of this program is to draw a stop sign using the turtle module


"""


import turtle as t

def draw_rectangle(width, height):
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.penup()

def draw_octagon(side_length):
    t.pendown()
    for _ in range(8):
        t.forward(side_length)
        t.left(45)
    t.penup()

def draw_stop_sign(side_length):
    # Move forward 3/8 of the side
    t.penup()
    t.forward(side_length * 3/8)
    t.pendown()
    
    # Draw the rectangle sign post
    draw_rectangle(side_length / 5, 2 * side_length)
    
    # Move to the top of the sign post
    t.left(90)
    t.forward(2 * side_length)
    t.right(90)
    
    # Draw the octagon for the stop sign
    draw_octagon(side_length)

# Example usage

if __name__ == "__main__":
    t.speed(1)
    t.color("red")
    draw_stop_sign(100)
    t.Screen().exitonclick()  



