import turtle 
import pandas      

# Set up the GUI
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Convert csv file into a list
df = pandas.read_csv("50_states.csv")
states = df.state.to_list()

# Keep track of states that have been guessed correctly
counted_states = []


while len(counted_states) < 50:

# Take input, and convert to title case
    answer = screen.textinput(title = f"{len(counted_states)}/50", prompt = "Name a state. Enter 'EXIT' to quit").title()

    # Exit program, and create a list of missing states
    if answer == "Exit":
        missing_states = [i for i in states if i not in counted_states]

        # Print out the states that were missed
        csv_file = pandas.DataFrame(missing_states)
        csv_file.to_csv("missing_states.csv")
        break
        

    # Check if answer is in list of states   
    if answer in states:
        counted_states.append(answer)
        states.remove(answer) 
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer)









