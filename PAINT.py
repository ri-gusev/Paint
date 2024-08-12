import turtle, random

# Размеры и цвет самого экрана(фона)
screen = turtle.Screen()
screen.screensize(900,600,'grey')
screen.title('PAINT 2.0')
screen.colormode(255)

#Полоска меню
square = turtle.Turtle()
square.shape('square')
square.hideturtle()
square.color('white')
square.shapesize(4,90)
square.penup()
square.goto(0,280)
square.showturtle()

#Фон инструмента кисть
br_bg = turtle.Turtle()
br_bg.hideturtle()
br_bg.color('grey')
br_bg.shape('square')
br_bg.shapesize(2,4)
br_bg.penup()
br_bg.goto(0,280)
br_bg.showturtle()

# Надпись кисть
br_bg_txt = turtle.Turtle()
br_bg_txt.hideturtle()
br_bg_txt.penup()
br_bg_txt.goto(0,272)
br_bg_txt.pendown()
br_bg_txt.color('black')
br_bg_txt.write('Кисть',align='center', font=('Arial',12,'bold'))

#Фон инструмента ластик
er_bg = turtle.Turtle()
er_bg.hideturtle()
er_bg.color('grey')
er_bg.shape('square')
er_bg.shapesize(2,4)
er_bg.penup()
er_bg.goto(100,280)
er_bg.showturtle()

# Надпись ластик
er_bg_txt = turtle.Turtle()
er_bg_txt.hideturtle()
er_bg_txt.penup()
er_bg_txt.goto(100,272)
er_bg_txt.pendown()
er_bg_txt.color('black')
er_bg_txt.write('Ластик',align='center', font=('Arial',12,'bold'))

#Сама ручка для кисти
brush = turtle.Turtle()
brush.speed(0)
brush.hideturtle()
brush.penup()
brush.shape('circle')
brush.shapesize(1)
brush.goto(0,238)
brush.pendown()
brush.showturtle()

#Сама ручка для ластика
er_brush = turtle.Turtle()
er_brush.speed(0)
er_brush.hideturtle()
er_brush.penup()
er_brush.shape('circle')
er_brush.color('grey','cyan')
er_brush.shapesize(1)
er_brush.pensize(15)
er_brush.goto(100,238)
er_brush.pendown()
er_brush.showturtle()


#Фон для кнопки 2px
fon2px = turtle.Turtle()
fon2px.speed(0)
fon2px.hideturtle()
fon2px.color('grey')
fon2px.shape('square')
fon2px.shapesize(2,2,0)
fon2px.penup()
fon2px.goto(-350,280)
fon2px.showturtle()

# размер пера надпись и кнопка 1
p2 = turtle.Turtle()
p2.hideturtle()
p2.penup()
p2.goto(-350,275)
p2.pendown()
p2.shape('square')
p2.shapesize(0.5)
p2.color('black')
p2.write('2' , align = 'center' , font = ('Аrial' , 14 ,
'bold'))
p2.penup()
p2.goto(-350,270)
p2.showturtle()

#Фон для кнопки 10px
fon10px = turtle.Turtle()
fon10px.speed(0)
fon10px.hideturtle()
fon10px.color('grey')
fon10px.shape('square')
fon10px.shapesize(2,2,0)
fon10px.penup()
fon10px.goto(-300,280)
fon10px.showturtle()

# размер пера надпись и кнопка 2
p10 = turtle.Turtle()
p10.hideturtle()
p10.penup()
p10.goto(-300,275)
p10.pendown()
p10.shape('square')
p10.shapesize(0.5)
p10.color('black')
p10.write('10' , align = 'center' , font = ('Аrial' , 14 ,
'bold'))
p10.penup()
p10.goto(-300,270)
p10.showturtle()

#Цвета
# кнопки цветов
c1 = turtle.Turtle()
c1.hideturtle()
c1.color('green')
c1.shape('square')
c1.shapesize(2,2,1)
c1.penup()
c1.goto(350,280)
c1.showturtle()
 
c2 = turtle.Turtle()
c2.hideturtle()
c2.color('red')
c2.shape('square')
c2.shapesize(2,2,1)
c2.penup()
c2.goto(300,280)
c2.showturtle()
 
c3 = turtle.Turtle()
c3.hideturtle()
c3.color('blue')
c3.shape('square')
c3.shapesize(2,2,1)
c3.penup()
c3.goto(250,280)
c3.showturtle()

c4 = turtle.Turtle()
c4.hideturtle()
c4.color('black')
c4.shape('square')
c4.shapesize(2,2,1)
c4.penup()
c4.goto(200,280)
c4.showturtle()

#Все что связано с карандашом
kb_bg = turtle.Turtle()
kb_bg.hideturtle()
kb_bg.color('grey')
kb_bg.penup()
kb_bg.shape('square')
kb_bg.shapesize(2,6)
kb_bg.setpos(-150,280)
kb_bg.showturtle()

kb_tx = turtle.Turtle()
kb_tx.hideturtle() 
kb_tx.color('black')
kb_tx.penup()
kb_tx.goto(-150,270)
kb_tx.pendown()
kb_tx.write('Карандаш', align= 'center',font= ('Arial',14,'bold'))

kb = turtle.Turtle()
kb.speed(0)
kb.shape('circle')
kb.shapesize(1)
kb.color('black')
kb.penup()
kb.setpos(-150,238)
kb.pendown()

#Функции для карандаша
def move_up():
    y = kb.ycor()
    kb.sety(y+20)
    kb.pencolor()
    kb.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
def move_down():
    y = kb.ycor()
    kb.sety(y-20)
    kb.pencolor()
    kb.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
def move_left():
    x = kb.xcor()
    kb.setx(x-20)
    kb.pencolor()
    kb.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
def move_right():
    x = kb.xcor()
    kb.setx(x + 20)
    kb.pencolor()
    kb.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))




#Перемещение мышкой
def drag(x,y):
    if y < 230:
        brush.ondrag(None)
        brush.setheading(brush.towards(x,y))
        brush.goto(x,y)
        brush.ondrag(drag)
        
def drag_ers(x,y):
    if y < 230:
        er_brush.ondrag(None)
        er_brush.setheading(er_brush.towards(x,y))
        er_brush.goto(x,y)
        er_brush.ondrag(drag_ers)

brush.ondrag(drag,1)
er_brush.ondrag(drag_ers,1)

def clickgreen(x,y):
    brush.color('green')
def clickred(x,y):
    brush.color('red')
def clickblue(x,y):
    brush.color('blue')
def clickblack(x,y):
    brush.color('black')
def size2(x,y):
    brush.pensize(2)
    kb.pensize(2)
def size10(x,y):
    brush.pensize(10)
    kb.pensize(10)

#Вызываем функции 
brush.ondrag(drag, 1)
er_brush.ondrag(drag_ers, 1)
c1.onclick(clickgreen, 1)
c2.onclick(clickred,1)
c3.onclick(clickblue,1)
c4.onclick(clickblack,1)
p2.onclick(size2, 1)
p10.onclick(size10, 1)

screen.listen()
screen.onkeypress(move_up,'Up')
screen.onkeypress(move_down,'Down')
screen.onkeypress(move_left,'Left')
screen.onkeypress(move_right,'Right')
 
turtle.mainloop()


