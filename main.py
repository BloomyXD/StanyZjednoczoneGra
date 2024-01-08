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
zrobione = []

csv = pandas.read_csv("50_states.csv")
lista = csv['state'].tolist()


while len(zrobione) < 50:
    stan = screen.textinput(title=f"{len(zrobione)}/50 Nazwa Stanu?", prompt="Jaki jest kolejny Stan?").title()

    if stan == 'Exit':
        braki = []
        for stann in lista:
            if stann not in zrobione:
                braki.append(stann)
        data = pandas.DataFrame(braki)
        data.to_csv("Stany Brakujące.csv")
        break

    if stan in lista:
        if stan not in zrobione:
            zrobione.append(stan)
            koordynaty = csv[csv.state == stan]
            print(koordynaty)
            żółw.goto(int(koordynaty.x.iloc[0]), int(koordynaty.y.iloc[0]))
            żółw.write(koordynaty.state.item())



