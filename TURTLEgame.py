import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("red")
drawing_board.title("MY GAme")


my_instance = turtle.Turtle()
def my_forward_func1():
    my_instance.forward(50)
def my_forward_func2():
    my_instance.left(10)
def my_forward_func3():
    my_instance.right(10)

def clear_screen():
    my_instance.clear()

def turtle_return_home():
    my_instance.home()
    # başladığı yere geri dönmesini sağlar
def turtle_penUP():
    my_instance.penup()

def turtle_penDOWN():
    my_instance.pendown()
drawing_board.listen()#bu fonksiyon ile tuşları dinlemeye alabiliriz
drawing_board.onkey(my_forward_func1,key="space")
drawing_board.onkey(my_forward_func2,key="Up")
drawing_board.onkey(my_forward_func3,key="Down")
drawing_board.onkey(clear_screen,key="c")
drawing_board.onkey(turtle_return_home,key="a")
drawing_board.onkey(turtle_penUP,key="s")
drawing_board.onkey(turtle_penDOWN,key="d")
#function isimlerini yazdıktan sonra () koyarsan çağırır ve olmaz

turtle.mainloop()
#mainloop sonsuz döngüye sokar
