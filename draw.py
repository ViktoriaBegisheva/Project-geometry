import turtle
 
def draw_p(p,text=False,color="black"):
    turtle.pu()
    turtle.setpos(p)
    turtle.pd()
    turtle.pencolor(color)
    turtle.dot()
    if text:
        turtle.write(text)
    turtle.pencolor("black")
    turtle.pu()
    return

def draw_points(S):
    for i in range(len(S)):
        draw_p(S[i],f'p{i}')
    return

def draw_line(p1,p2,color="black"):
    turtle.pu()
    turtle.setpos(p1)
    turtle.pd()
    turtle.pencolor(color)
    turtle.goto(p2)
    turtle.up()
    turtle.pencolor("black")
    return

def draw_lines_qsort(S,q):
    for p in S:
        draw_line(q,p,"grey")
    return

def set_speed(n):
    turtle.speed(n)
    return



