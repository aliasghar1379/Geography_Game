import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. status Game")
image = "blank_states_img.gif"
screen.addshape(image)

list_state = [0]
score = 1

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state
end_game = False
while not end_game:
    answer_state = (screen.textinput(title=f"{score-1}/{len(states)} Guess the state", prompt="What's another state's name? ")).title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in list_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        end_game = True
    for state in states:
        if answer_state == state:
            if score > 50:
                turtle.clear()
                turtle.write("You did it...well done.")
            else:
                list_state.append(answer_state)
                score = len(list_state)
                st = data[data.state == f"{state}"]
                x_cor = int(st.x)
                y_cor = int(st.y)
                turtle.tracer(0)
                turtle.penup()
                turtle.goto(x_cor, y_cor)
                turtle.write(f"{state}",align="center")
