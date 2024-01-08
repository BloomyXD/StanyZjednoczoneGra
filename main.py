import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
żółw = turtle.Turtle()
żółw.hideturtle()
żółw.penup()

csv = pandas.read_csv("50_states.csv")
lista = csv['state'].tolist()
x = csv['x'].tolist()
y = csv['y'].tolist()
print(lista)

stan = screen.textinput(title="Nazwa Stanu?", prompt="Jaki jest kolejny Stan?").title()
print(stan)

if stan in lista:
    żółw.goto(172,52)
    żółw.write(stan)



turtle.mainloop()
