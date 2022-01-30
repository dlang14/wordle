import turtle, random
import words
import enchant

def display_keyboard():
    y = -300
    x = -375
    for i in range(0,len(keyboard)):
        turtle.penup()
        turtle.goto(x,y)
        turtle.write(keyboard[i].upper(),font=("Verdana", 30, "normal"), align='center')
        tup = (keyboard[i],x,y)
        keyboard_pos.append(tup)
        x = x + 30

def draw_square(x,y,col,key): # takes in x,y coordinates and a color
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(col) # set the fillcolor
    turtle.begin_fill() # start the filling color
    if key == False:
        for i in range(4):     # drawing the square
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill() # ending the filling of the color
    else:
        for i in range(4):     # drawing the square
            turtle.forward(30)
            turtle.right(90)
        turtle.end_fill()

def input_guess(prompt):
    my_input = turtle.textinput("5 letter word", prompt)
    if check_valid_word(my_input):
        return my_input.lower()
    else:
        while check_valid_word(my_input) == False:
            my_input = turtle.textinput("5 letter word", prompt)
            if check_valid_word(my_input):
                return my_input.lower()

def check_valid_word(input):
    if ((len(input) == 5) & (d.check(input) == True)):
        return True
    else:
        return False

def check_guess(my_input,answer,y):
    count = 0 #Need a count, because of for loop used
    x = -250 # x location

    for i in my_input:
        if i == answer[count]:
            draw_square(x,y,"green",False) #exact character match draws a green square
            write_letter(x+10,y-55,i,50)
            tup = (i, 'green')
            guess_list.append(tup)
        elif i in answer:
            draw_square(x,y,"yellow",False) #else if character anywhere in word draws yellow
            write_letter(x+10,y-55,i,50)
            tup = (i, 'yellow')
            guess_list.append(tup)
        else:
            draw_square(x,y,"red",False) # otherwise draws red
            write_letter(x+10,y-55,i,50)
            tup = (i, 'red')
            guess_list.append(tup)

        count+=1 # add 1 to the count
        x += 75 # move x coordinate along by 75
    turtle.penup() #Moves the turtle penup
    turtle.goto(x,y-25) #Moves it slightly down for the word
    turtle.write(my_input,font=("Verdana", 15, "normal")) # font verdana, size 15, normal style

def update_keyboard(guess_list):
    for i in range(0,len(guess_list)):
        count = 0
        for j in range(0,len(keyboard_pos)):
            if guess_list[i][0] == keyboard_pos[j][0]:
                if count == 0:
                    draw_square(keyboard_pos[j][1] - 15, keyboard_pos[j][2] + 32, guess_list[i][1], True)
                    count = count + 1

def write_letter(x,y,letter,font_size):
    turtle.penup() #Moves the turtle penup
    turtle.goto(x+15,y) #Moves it slightly down for the word
    turtle.write(letter.upper(),align="center",font=("Verdana", font_size, "normal"))

def initialize_turtle():
    turtle.speed(speed=0)
    turtle.Screen().bgcolor("grey")

if __name__ == "__main__":
    initialize_turtle()
    d = enchant.Dict("en_US")
    answer = words.get_random_word()
    y = 250 # y location
    print(answer)
    keyboard = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    keyboard_pos = []
    guess_list = []

    display_keyboard()
    for i in range(6): #Where the program starts
        guess_prompt = "What is guess "+str(i+1)+"?" #Makes a nice string for the prompt
        my_input = input_guess(guess_prompt) #calls input_guess function
        check_guess(my_input,answer,y) #checks the guess
        update_keyboard(guess_list)
        guess_list = []
        display_keyboard()
        y -= 75 #y down by 75
        if my_input == answer:
            turtle.penup()
            turtle.goto(-350,-250) #Always draws the congratulations in the same place
            turtle.write("GGs!",font=("Verdana", 42, "normal"))
            break
    else: #Only runs if the for loop executes completely. i.e. You've used all your guesses.
        turtle.penup()
        turtle.goto(-350,-250)
        turtle.write(answer + " dumbass",font=("Verdana", 42, "normal"))
    turtle.done() #Needs if you are using Pycharm and some other Python editors.
