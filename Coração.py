from turtle import Turtle, done

cor_caneta = 'red'
cor_texto = 'black'
mensagem = "Te amo!"
angulo_curva = 1
distancia_curva = 1

def curve(angle, distance):
    for _ in range(200):
        pen.right(angle)
        pen.forward(distance)

def heart():
    pen.fillcolor(cor_caneta)
    pen.pencolor(cor_caneta)
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve(angulo_curva, distancia_curva)
    pen.left(120)
    curve(angulo_curva, distancia_curva)
    pen.forward(112)
    pen.end_fill()

def txt():
    pen.up()
    pen.setpos(-35, 90)
    pen.down()
    pen.color(cor_texto)
    pen.write(mensagem, font=("Verdana", 12, "bold"))

pen = Turtle()
heart()
txt()
pen.ht()
done()