#######################################################################################
# Draw words module with turble
# This Module draw 'a' to 'z' letters with the space ' ' for separation
#
# Created by Yeun Jae, Jung in September of 2020 (Barcelona, Spain)
# Contact
#   email: jungyeunjae@gmail.com
#   github: https://github.com/JungPablo
#######################################################################################

from turtle import *


pen = Turtle()
pen.color('yellow')
pen.pensize(1)
pen.speed(0)
pen.shape('classic')
pen.hideturtle()

# Window
window = pen.getscreen()
window.screensize()
window.setup(width = 1.0, height = 1.0)
window.title('DRAW YOUR WORDS')
window.bgcolor('black')

height = 100
width = height/2

x1 = width / 4
x2 = width / 2
x3 = width * 3/4
x4 = width
y1 = height / 4
y2 = height / 2
y3 = height * 3/4
y4 = height




#####################################################################
# Letter draw functions
#####################################################################

def draw_a(x, y):
    pen.penup()
    pen.goto(x+x2, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x+x2, y+y4)
    pen.goto(x+x4, y)
    pen.penup()
    pen.goto(x+x1, y+y2)
    pen.pendown()
    pen.goto(x+x3, y+y2)
    pen.penup()

def draw_b(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.setheading(180)
    pen.goto(x, y)
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x2, y+y4)
    pen.circle(x2, -180)
    pen.setheading(180)
    pen.goto(x, y+y2)
    pen.goto(x+x2, y+y2)
    pen.circle(x2, -180)
    pen.goto(x, y)
    pen.penup()

def draw_c(x, y):
    pen.penup()
    pen.goto(x+x4, y+y3)
    pen.pendown()
    pen.setheading(90)
    pen.circle(x2, 180)
    pen.goto(x, y+y1)
    pen.setheading(270)
    pen.circle(x2, 180)
    pen.penup()

def draw_d(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y+y4)
    pen.goto(x+x2, y+y4)
    pen.setheading(180)
    pen.circle(x2, -90)
    pen.goto(x+x4, y+y1)
    pen.setheading(90)
    pen.circle(x2, -90)
    pen.goto(x, y)
    pen.penup()

def draw_e(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x4, y+y4)
    pen.goto(x, y+y4)
    pen.goto(x, y)
    pen.goto(x+x4, y)
    pen.penup()
    pen.goto(x, y+y2)
    pen.pendown()
    pen.goto(x+x4, y+y2)
    pen.penup()
    
def draw_f(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x4, y+y4)
    pen.goto(x, y+y4)
    pen.goto(x, y)
    pen.goto(x, y+y2)
    pen.goto(x+x4, y+y2)
    pen.penup()

def draw_g(x, y):
    pen.penup()
    pen.goto(x+x4, y+y3)
    pen.pendown()
    pen.setheading(90)
    pen.circle(x2, 180)
    pen.goto(x, y+y1)
    pen.circle(x2, 180)
    pen.penup()
    pen.goto(x+x2, y+y2)
    pen.pendown()
    pen.goto(x+x4, y+y2)
    pen.goto(x+x4, y+y1)
    pen.penup()

def draw_h(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y+y2)
    pen.goto(x+x4, y+y2)
    pen.penup()
    pen.goto(x+x4, y+y4)
    pen.pendown()
    pen.goto(x+x4, y)
    pen.penup()

def draw_i(x, y):
    pen.penup()
    pen.goto(x+x2, y+y4)
    pen.pendown()
    pen.goto(x+x2, y)
    pen.penup()

def draw_j(x, y):
    pen.penup()
    pen.goto(x+x4, y+y4)
    pen.pendown()
    pen.goto(x+x4, y+y1)
    pen.setheading(90)
    pen.circle(x2, -180)
    pen.penup()

def draw_k(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y+y2)
    pen.goto(x+x4, y+y4)
    pen.goto(x, y+y2)
    pen.goto(x+x4, y)
    pen.penup()

def draw_l(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x+x4, y)
    pen.penup()

def draw_m(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y+y4)
    pen.goto(x+x2, y+y2)
    pen.goto(x+x4, y+y4)
    pen.goto(x+x4, y)
    pen.penup()

def draw_n(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y+y4)
    pen.goto(x+x4, y)
    pen.penup()
    pen.goto(x+x4, y+y4)
    pen.pendown()
    pen.goto(x+x4, y)
    pen.penup()

def draw_ñ(x, y):
    pen.penup()
    pen.goto(x, y+y4*4/5)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y+y4*4/5)
    pen.goto(x+x4, y)
    pen.penup()
    pen.goto(x+x4, y+y4*4/5)
    pen.pendown()
    pen.goto(x+x4, y)
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x4, y+y4)
    pen.penup()

def draw_o(x, y):
    pen.penup()
    pen.goto(x+x4, y+y3)
    pen.setheading(90)
    pen.pendown()
    pen.circle(x2, 180)
    pen.goto(x, y+y1)
    pen.setheading(270)
    pen.circle(x2, 180)
    pen.goto(x+x4, y+y3)
    pen.penup()

def draw_p(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y+y4)
    pen.goto(x+x2, y+y4)
    pen.setheading(180)
    pen.circle(x2, -180)
    pen.goto(x, y+y2)
    pen.penup()

def draw_q(x, y):
    pen.penup()
    pen.goto(x+x4, y+y3)
    pen.setheading(90)
    pen.pendown()
    pen.circle(x2, 180)
    pen.goto(x, y+y1)
    pen.setheading(270)
    pen.circle(x2, 180)
    pen.goto(x+x4, y+y3)
    pen.penup()
    pen.goto(x+x2, y+y1)
    pen.pendown()
    pen.goto(x+x4, y)
    pen.penup()


def draw_r(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y+y4)
    pen.goto(x+x2, y+y4)
    pen.setheading(180)
    pen.circle(x2, -180)
    pen.goto(x, y+y2)
    pen.goto(x+x4, y)
    pen.penup()

def draw_s(x, y):
    pen.penup()
    pen.goto(x+x4, y+y3)
    pen.pendown()
    pen.setheading(90)
    pen.circle(x2, 270)
    pen.setheading(180)
    pen.circle(x2, -270)
    pen.penup()

def draw_t(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x4, y+y4)
    pen.goto(x+x2, y+y4)
    pen.goto(x+x2, y)
    pen.penup()

def draw_u(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y+y1)
    pen.setheading(270)
    pen.circle(x2, 180)
    pen.goto(x+x4, y+y4)
    pen.penup()

def draw_v(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x2, y)
    pen.goto(x+x4, y+y4)
    pen.penup()

def draw_w(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x+x2, y+y2)
    pen.goto(x+x4, y)
    pen.goto(x+x4, y+y4)
    pen.penup()

def draw_x(x, y):
    pen.penup()
    pen.goto(x+x4, y+y4)
    pen.pendown()
    pen.goto(x, y)
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x4, y)
    pen.penup()

def draw_y(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x2, y+y2)
    pen.goto(x+x4, y+y4)
    pen.goto(x+x2, y+y2)
    pen.goto(x+x2, y)
    pen.penup()

def draw_z(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x4, y+y4)
    pen.goto(x, y)
    pen.goto(x+x4, y)
    pen.penup()

def draw_apo(x, y):
    pen.penup()
    pen.goto(x+x2, y+y4)
    pen.pendown()
    pen.goto(x+x2, y+y3)
    pen.penup()

def draw_qtn(x, y):
    pen.penup()
    pen.goto(x, y+y3)
    pen.setheading(270)
    pen.pendown()
    pen.circle(x2, -270)
    pen.goto(x+x2, y+y1)
    pen.penup()
    pen.goto(x+x2, y)
    pen.pendown()
    pen.circle(x1/2)
    pen.penup()

def draw_excl(x, y):
    pen.penup()
    pen.goto(x+x2, y+y4)
    pen.pendown()
    pen.goto(x+x2, y+y1)
    pen.penup()
    pen.goto(x+x2, y)
    pen.setheading(0)
    pen.pendown()
    pen.circle(x1/2)
    pen.penup()

def draw_0(x, y):
    pen.penup()
    pen.goto(x+x4, y+y3)
    pen.setheading(90)
    pen.pendown()
    pen.circle(x2, 180)
    pen.goto(x, y+y1)
    pen.setheading(270)
    pen.circle(x2, 180)
    pen.goto(x+x4, y+y3)
    pen.penup()

def draw_1(x, y):
    pen.penup()
    pen.goto(x+x2, y+y4)
    pen.pendown()
    pen.goto(x+x2, y)
    pen.penup()

def draw_2(x, y):
    pen.penup()
    pen.goto(x, y+y3)
    pen.pendown()
    pen.setheading(270)
    pen.circle(x2, -200)
    pen.goto(x, y)
    pen.goto(x+x4, y)
    pen.penup()

def draw_3(x, y):
    pen.penup()
    pen.goto(x, y+y3)
    pen.pendown()
    pen.setheading(270)
    pen.circle(x2, -270)
    pen.setheading(180)
    pen.circle(x2, -270)
    pen.penup()

def draw_4(x, y):
    pen.penup()
    pen.goto(x+x3, y+y4)
    pen.pendown()
    pen.goto(x, y+y1)
    pen.goto(x+x4, y+y1)
    pen.penup()
    pen.goto(x+x3, y+y2)
    pen.pendown()
    pen.goto(x+x3, y)
    pen.penup()

def draw_5(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x, y+y4*5/8)
    pen.goto(x+x2, y+y4*5/8)
    pen.setheading(180)
    pen.circle(x2, -90)
    pen.goto(x+x4, y+y1)
    pen.setheading(90)
    pen.circle(x2, -180)
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x4, y+y4)
    pen.penup()

def draw_6(x, y):
    pen.penup()
    pen.goto(x+x4, y+y4)
    pen.pendown()
    pen.goto(x+x1, y+y4*7/16)
    pen.setheading(225)
    pen.circle(x2)
    pen.penup()

def draw_7(x, y):
    pen.penup()
    pen.goto(x, y+y4)
    pen.pendown()
    pen.goto(x+x4, y+y4)
    pen.goto(x, y)
    pen.penup()

def draw_8(x, y):
    pen.penup()
    pen.goto(x+x2, y+y4)
    pen.pendown()
    pen.setheading(180)
    pen.circle(x2, 180)
    pen.setheading(180)
    pen.circle(x2, -360)
    pen.setheading(0)
    pen.circle(x2, 180)
    pen.penup()

def draw_9(x, y):
    pen.penup()
    pen.goto(x+x3, y+y4*9/16)
    pen.pendown()
    pen.setheading(45)
    pen.circle(x2)
    pen.goto(x, y)
    pen.penup()

def top_line(x, y, col):
    pen.penup()
    pen.goto(x-5, y+y4+5)
    pen.pendown()
    pen.goto(x+x4*col, y+y4+5)
    pen.penup()

def button_line(x, y, col):
    pen.penup()
    pen.goto(x-5, y-5)
    pen.pendown()
    pen.goto(x+x4*col, y-5)
    pen.penup()

#####################################################################
# Main draw function
#####################################################################

def draw(words):
# This is a draw function. Receive the parameter words and draw the words using the turtle library
        row = 1
        order_char = 0
        column = 1
        nxt_row = 0
        space = x4
        screen_width = 1300
        screen_height = 700
        letters_qty = screen_width//(2*x4)
        init_x = -(letters_qty//2)*2*x4-0.5*x4
        init_y = (screen_height//2)-1.5*y4
        pen.penup()
        clearscreen
        for i in words: # Iteration of words
            if row <= screen_height//(1.5*y4): # Not EOL
                if i != ' ': # If char is no emphty
                    start_x = init_x+space*order_char # Set x start position
                    start_y = init_y-nxt_row # Set y start position
                    dic_draw_func[i](start_x, start_y) # with i letter key call draw function with x and y start position
                    order_char += 2 # Add 2 width for each letter draw
                    column += 1 # Add 1 to column nbr
                else:
                    order_char += 2 # Add 2 width for each letter draw
                    column += 1 # Add 1 to column nbr
                if column == (row*letters_qty)+1: # If End Of Column
                    order_char = 0 # Return to 1st column
                    nxt_row += 1.5*y4 # Add 1.5 height to nxt_row
                    row += 1 # Add nbr row

        # Exit
        onkeypress(bye, 'q')
        listen()
        done()
    


# Dictionary with the letter key and letter draw fucntion
dic_draw_func = {
    'a':draw_a,
    'á':draw_a,
    'b':draw_b,
    'c':draw_c,
    'd':draw_d,
    'e':draw_e,
    'é':draw_e,
    'f':draw_f,
    'g':draw_g,
    'h':draw_h,
    'i':draw_i,
    'í':draw_i,
    'j':draw_j,
    'k':draw_k,
    'l':draw_l,
    'm':draw_m,
    'n':draw_n,
    'ñ':draw_ñ,
    'o':draw_o,
    'ó':draw_o,
    'p':draw_p,
    'q':draw_q,
    'r':draw_r,
    's':draw_s,
    't':draw_t,
    'u':draw_u,
    'ú':draw_u,
    'v':draw_v,
    'w':draw_w,
    'x':draw_x,
    'y':draw_y,
    'z':draw_z,
    ' ':'',
    "'":draw_apo,
    '?':draw_qtn,
    '!':draw_excl,
    '0':draw_0,
    '1':draw_1,
    '2':draw_2,
    '3':draw_3,
    '4':draw_4,
    '5':draw_5,
    '6':draw_6,
    '7':draw_7,
    '8':draw_8,
    '9':draw_9,
}


