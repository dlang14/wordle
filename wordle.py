import turtle, random
import words
import enchant

def display_keyboard():
    y = -300
    x = -375
    # Loop through alphabet so each letter is assigned an x,y position
    for i in range(0,len(keyboard)):
        turtle.penup()
        turtle.goto(x,y)
        turtle.write(keyboard[i].upper(),font=("Verdana", 30, "normal"), align='center')
        tup = (keyboard[i],x,y)
        keyboard_pos.append(tup)
        x = x + 30

def draw_square(x,y,col,key): # takes in x,y coordinates, color, key is true if for keyboard
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(col)
    turtle.begin_fill()
    # check if we are drawing a main square or a keyboard square
    if key == False:
        for i in range(4):
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()
    else:
        for i in range(4):  # Keyboard squares are smaller, yay
            turtle.forward(30)
            turtle.right(90)
        turtle.end_fill()

def input_guess(prompt):
    my_input = turtle.textinput("5 letter word", prompt)
    if check_valid_word(my_input): # check if input is legit
        return my_input.lower()
    else:
        while check_valid_word(my_input) == False: # keep prompting dumb user for valid word
            my_input = turtle.textinput("5 letter word", prompt)
            if check_valid_word(my_input):
                return my_input.lower()

def check_valid_word(input):
    if ((len(input) == 5) & (d.check(input) == True)): # checks if word is 5 letters and in dictionary
        return True
    else:
        return False

def check_guess(my_input,answer,y):
    count = 0
    x = -250

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

        count+=1
        x += 75 # move x coordinate along by 75
    turtle.penup()
    turtle.goto(x,y-25)
    turtle.write(my_input,font=("Verdana", 15, "normal"))

def update_keyboard(guess_list):
    # here we are figuring out what color box should be drawn around keyboard letters
    for i in range(0,len(guess_list)):
        count = 0 # keeping count so we dont draw multiple squares around a letter
        for j in range(0,len(keyboard_pos)):
            if guess_list[i][0] == keyboard_pos[j][0]:
                if count == 0:
                    draw_square(keyboard_pos[j][1] - 15, keyboard_pos[j][2] + 32, guess_list[i][1], True)
                    count = count + 1

def write_letter(x,y,letter,font_size):
    turtle.penup()
    turtle.goto(x+15,y)
    turtle.write(letter.upper(),align="center",font=("Verdana", font_size, "normal"))

def initialize_turtle():
    write_letter(-50,275,"wordle 2.0", 75)
    turtle.speed(speed=0)
    turtle.Screen().bgcolor("grey")

if __name__ == "__main__":
    initialize_turtle()
    d = enchant.Dict("en_US") # load in english dictionary to cross reference guesses
    answer = words.get_random_word()
    y = 250
    print(answer) # remove if you dont want answer in terminal
    keyboard = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    keyboard_pos = []
    guess_list = []

    display_keyboard() # Add keyboard to screen
    for i in range(6): #Where the program starts
        guess_prompt = "What is guess "+str(i+1)+"?" # prompt user for input
        my_input = input_guess(guess_prompt)
        check_guess(my_input,answer,y)
        update_keyboard(guess_list) # draw squares around keyboard letters based on guess
        guess_list = []
        display_keyboard() # need to redraw keyboard over the boxed letters
        y -= 75 #y down by 75
        if my_input == answer:
            turtle.penup()
            turtle.goto(-350,-250)
            turtle.write("GGs!",font=("Verdana", 42, "normal"))
            break
    else: # for when you guess wrong 6 times
        turtle.penup()
        turtle.goto(-350,-250)
        turtle.write(answer + " dumbass",font=("Verdana", 42, "normal"))
    turtle.done()
