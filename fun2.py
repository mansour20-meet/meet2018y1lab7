import turtle
turtle.goto(0,0)

UP = 0
down = 1
right = 2
left = 3
direction = None

def up():
    global direction
    UP = 0
    print("You pressed the up key.")
    
turtle.onkey(up, "Up") 
turtle.listen()

def on_move():
    def down():
        global direction
        direction = down
        print("You pressed the down key.")

turtle.onkey(down, "Down") 
turtle.listen()

def on_move():
    def right():
        global direction
        direction =right 
        print("You pressed the right key.")

turtle.onkey(right, "Right") 
turtle.listen()

def on_move():
    def left():
        global direction
        direction = left
        print("You pressed the left key.")

turtle.onkey(left, "Left") 
turtle.listen()
    
