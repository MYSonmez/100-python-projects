STATE_FONT = ("monaco", 8, "bold")
GAME_OVER_FONT = ("monaco", 30, "bold")

import pandas
import turtle

image = "project-024/project/blank_states_img.gif"
background = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
background.shape(image)
screen.setup(width=725, height=491)

data = pandas.read_csv("project-024/project/50_states.csv")
states_name = data.state
states_name_list = states_name.to_list()

succesful_guess = 0
guessed_states = []
while succesful_guess != 50:
    guess = screen.textinput(
        title=f"{succesful_guess}/50 Make Your Guess!",
        prompt="To win you must guess over than 15 (Type 'exit' to exit)",
    )
    if guess != None:
        guess = guess.title()
    else:
        break
    if guess == "Exit":
        break
    while guess != "Exit" and (
        guess not in states_name_list or guess in guessed_states
    ):
        guess = screen.textinput(
            title=f"{succesful_guess}/50 Make Your Guess!",
            prompt="To win you must guess over than 15 (Type 'exit' to exit)",
        )
        if guess != None:
            guess = guess.title()
        else:
            break
    if guess == "Exit":
        break
    succesful_guess += 1
    guessed_states.append(guess)
    state_name = turtle.Turtle(visible=False)
    state_name.penup()
    x_cor = int(data[states_name == guess].x.iloc[0])
    y_cor = int(data[states_name == guess].y.iloc[0])
    state_name.goto(x=x_cor, y=y_cor)
    state_name.write(arg=guess, align="center", font=STATE_FONT)

game_over_text = turtle.Turtle(visible=False)
game_over_text.penup()
game_over_text.goto(0, 120)
if succesful_guess >= 15:
    game_over_text.write(
        arg=f"You Win!\nFinal Score: {succesful_guess}",
        align="center",
        font=GAME_OVER_FONT,
    )
else:
    game_over_text.write(
        arg=f"You Lose!\nFinal Score: {succesful_guess}",
        align="center",
        font=GAME_OVER_FONT,
    )
screen.exitonclick()

missing_states = [state for state in states_name_list if state not in guessed_states]

df = pandas.DataFrame(missing_states)
df.to_csv("project-024/project/not_guessed_states.csv")
