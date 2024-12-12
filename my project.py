import turtle

laki = turtle.Turtle()
laki.shape('turtle')
laki.color('#FFA07A')
laki.pensize(10)
laki.shapesize(stretch_wid=3, stretch_len=3, outline=2)
for _ in range(2):
    laki.forward(150)  # حرکت به جلو به اندازه 150 واحد
    laki.right(90)     # چرخش 90 درجه به سمت راست
    laki.forward(100)  # حرکت به جلو به اندازه 100 واحد
    laki.right(90)     # چرخش 90 درجه به سمت راست

turtle.bgcolor('lightgreen')

turtle.mainloop()