import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. State game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

game_on = True
answer_state = []
while game_on:

    answer = screen.textinput(title=f"{len(answer_state)}/50 of states correct", prompt="What's another state name").title()

    state_data = pandas.read_csv("50_states.csv")
    all_state = state_data.state.to_list()

    if answer == "Exit":
        missing_state = []
        for state in all_state:
            if state not in answer_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_state and answer not in answer_state:
        answer_state.append(answer)
        state_row = state_data[state_data["state"] == answer]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        new_x = state_row.x.item()
        new_y = state_row.y.item()


        t.goto(new_x, new_y)
        t.write(state_row.state.item())


        if len(answer_state) == 50:
            game_on = False



