# Jack Rosetti
# Period 4
# 11/19/17

from tkinter import *

flag = 0

def checkValues():
    #checks for ties



    #TODO 1 Create "if statements" for when X or Y gets three in a row via row 1.
    #         Include "if statement" for when X gets 3 in a row.
    #         Include "if statement" for when Y gets 3 in a row.
    #         In both cases, the labelTitle should change and address who won or a tie.
    #         In both cases, call "disableButtons()" after a winner is declared.
    if(button_0.cget('bg')=='red' and button_1.cget('bg')=='red' and button_2.cget('bg')=='red'):
        disableButtons()
        LabelTitle.config(text="Red wins!")
    elif( button_0.cget('bg')=='blue'and button_1.cget('bg')=='blue'and button_2.cget('bg')=='blue'):
        LabelTitle.config(text="Blue wins!")
    # TODO #2 Create "if statements" for when X or Y gets three in a row via row 2.
    #         Include "if statement" for when X gets 3 in a row.
    #         Include "if statement" for when Y gets 3 in a row.
    #         In both cases, the labelTitle should change and address who won or a tie.
    #         In both cases, call "disableButtons()" after a winner is declared.
    elif (button_3.cget('bg') == 'red' and button_4.cget('bg') == 'red' and button_5.cget('bg') == 'red'):
        disableButtons()
        LabelTitle.config(text="Red wins!")
    elif (button_3.cget('bg') == 'blue' and button_4.cget('bg') == 'blue' and button_5.cget('bg') == 'blue'):
            disableButtons()
            LabelTitle.config(text="Blue wins!")

    # TODO #3 Create "if statements" for when X or Y gets three in a row via row 3.
    #         Include "if statement" for when X gets 3 in a row.
    #         Include "if statement" for when Y gets 3 in a row.
    #         In both cases, the labelTitle should change and address who won or a tie.
    #         In both cases, call "disableButtons()" after a winner is declared.
    elif (button_6.cget('bg') == 'blue' and button_7.cget('bg') == 'blue' and button_8.cget('bg') == 'blue'):
        disableButtons()
        LabelTitle.config(text="Blue wins!")
    elif (button_6.cget('bg') == 'red' and button_7.cget('bg') == 'red' and button_8.cget('bg') == 'red'):
        disableButtons()
        LabelTitle.config(text="Red wins!")

    # TODO #4 Create "if statements" for when X or Y gets three in a row via column 1.
    #         Include "if statement" for when X gets 3 in a row.
    #         Include "if statement" for when Y gets 3 in a row.
    #         In both cases, the labelTitle should change and address who won or a tie.
    #         In both cases, call "disableButtons()" after a winner is declared.
    elif (button_0.cget('bg') == 'red' and button_3.cget('bg') == 'red' and button_6.cget('bg') == 'red'):
        disableButtons()
        LabelTitle.config(text="Red wins!")
    elif (button_0.cget('bg') == 'blue' and button_3.cget('bg') == 'blue' and button_6.cget('bg') == 'blue'):
        disableButtons()
        LabelTitle.config(text="Blue wins!")

    # TODO #5 Create "if statements" for when X or Y gets three in a row via column 2.
    #         Include "if statement" for when X gets 3 in a row.
    #         Include "if statement" for when Y gets 3 in a row.
    #         In both cases, the labelTitle should change and address who won or a tie.
    #         In both cases, call "disableButtons()" after a winner is declared.
    elif (button_1.cget('bg') == 'red' and button_4.cget('bg') == 'red' and button_7.cget('bg') == 'red'):
        disableButtons()
        LabelTitle.config(text="Red wins!")
    elif (button_1.cget('bg') == 'blue' and button_4.cget('bg') == 'blue' and button_7.cget('bg') == 'blue'):
            disableButtons()
            LabelTitle.config(text="Blue wins!")
    # TODO #6 Create "if statements" for when X or Y gets three in a row via column 3.
    #         Include "if statement" for when X gets 3 in a row.
    #         Include "if statement" for when Y gets 3 in a row.
    #         In both cases, the labelTitle should change and address who won or a tie.
    #         In both cases, call "disableButtons()" after a winner is declared.
    elif (button_2.cget('bg') == 'red' and button_5.cget('bg') == 'red' and button_8.cget('bg') == 'red'):
                disableButtons()
                LabelTitle.config(text="Red wins!")
    elif (button_2.cget('bg') == 'blue' and button_5.cget('bg') == 'blue' and button_8.cget('bg') == 'blue'):
        disableButtons()
        LabelTitle.config(text="Blue wins!")
    # TODO #7 Create "if statement" for when X or Y gets three in a row via diagonally from left to right.
    #         Include "if statement" for when X gets 3 in a row.
    #         Include "if statement" for when Y gets 3 in a row.
    #         In both cases, the labelTitle should change and address who won or a tie.
    #         In both cases, call "disableButtons()" after a winner is declared.
    elif (button_0.cget('bg') == 'red' and button_4.cget('bg') == 'red' and button_8.cget('bg') == 'red'):
            disableButtons()
            LabelTitle.config(text="Red wins!")
    elif (button_0.cget('bg') == 'blue' and button_4.cget('bg') == 'blue' and button_8.cget('bg') == 'blue'):
                disableButtons()
                LabelTitle.config(text="Blue wins!")
    # TODO #8 Create "if statement" for when X or Y gets three in a row via diagonally from right to left.
    #         Include "if statement" for when X gets 3 in a row.
    #         Include "if statement" for when Y gets 3 in a row.
    #         In both cases, the labelTitle should change and address who won or a tie.
    #         In both cases, call "disableButtons()" after a winner is declared.
    elif (button_2.cget('bg') == 'blue' and button_4.cget('bg') == 'blue' and button_6.cget('bg') == 'blue'):
            disableButtons()
            LabelTitle.config(text="Blue wins!")
    elif (button_2.cget('bg') == 'red' and button_4.cget('bg') == 'red' and button_6.cget('bg') == 'red'):
            disableButtons()
            LabelTitle.config(text="Red wins!")
    elif(button_0.cget('state')=='disabled' and button_1.cget('state')=='disabled' and button_2.cget('state')=='disabled' and button_3.cget('state')=='disabled' and button_4.cget('state')=='disabled' and button_5.cget('state')=='disabled' and button_6.cget('state')=='disabled' and button_7.cget('state')=='disabled' and button_8.cget('state')=='disabled'):
            LabelTitle.config(text="This is a tie!")


    if LabelTitle.cget('text')== 'tie' or LabelTitle.cget('text')== 'Red wins!' or LabelTitle.cget('text')== 'Blue wins!':
        button_reset.grid(row=0, column=2)

def disableButtons():
    # TODO #10 Disable all buttons.
    button_0.config(state="disabled")
    button_1.config(state="disabled")
    button_2.config(state="disabled")
    button_3.config(state="disabled")
    button_4.config(state="disabled")
    button_5.config(state="disabled")
    button_6.config(state="disabled")
    button_7.config(state="disabled")
    button_8.config(state="disabled")

    return

def reset():
    button_reset.grid_remove()
    LabelTitle.config(text="This is a Tic Tac Toe game!")
    button_0.config(state='active', bg = "#f0f0f0", text="")
    button_1.config(state='active', bg = "#f0f0f0", text="")
    button_2.config(state='active', bg = "#f0f0f0", text="")
    button_3.config(state='active', bg = "#f0f0f0", text="")
    button_4.config(state='active', bg = "#f0f0f0", text="")
    button_5.config(state='active', bg = "#f0f0f0", text="")
    button_6.config(state='active', bg = "#f0f0f0", text="")
    button_7.config(state='active', bg = "#f0f0f0", text="")
    button_8.config(state='active', bg = "#f0f0f0", text="")
    return

def buttonClicked(Button):
    global flag
    if flag == 0:
        # TODO #11 Configure the button to show a letter, a color, and be disabled.
        Button.config(bg="blue", text="X",state="disabled")
        flag = 1
    else:
        # TODO #12 Configure the button to show a letter, a color, and be disabled.
        Button.config(bg="red", text="O", state="disabled")
        flag=0
    checkValues()

root = Tk()
# TODO #13 Create a label and give it a text value. Call the label: labelTitle.
LabelTitle = Label(root, text="This is Tic Tac Toe!")

# TODO #14 Create button_0. Give it a width of 10 and height of 5.
button_0 = Button(root, width=10, height = 5)

# TODO #15 Configure button_0 and pass it the following argument: command=lambda: buttonClicked(button_0)
button_0.config(command=lambda: buttonClicked(button_0))
# TODO #16 Repeat for buttons 1 through 8 using the same naming convention.
button_0.config(command=lambda: buttonClicked(button_0))
button_1 = Button(root, width=10, height=5)
button_1.config(command=lambda: buttonClicked(button_1))
button_2 = Button(root, width=10, height=5)
button_2.config(command=lambda: buttonClicked(button_2))
button_3 = Button(root, width=10, height=5)
button_3.config(command=lambda: buttonClicked(button_3))
button_4 = Button(root, width=10, height=5)
button_4.config(command=lambda: buttonClicked(button_4))
button_5 = Button(root, width=10, height=5)
button_5.config(command=lambda: buttonClicked(button_5))
button_6 = Button(root, width=10, height=5)
button_6.config(command=lambda: buttonClicked(button_6))
button_7 = Button(root, width=10, height=5)
button_7.config(command=lambda: buttonClicked(button_7))
button_8 = Button(root, width=10, height=5)
button_8.config(command=lambda: buttonClicked(button_8))

button_reset = Button(width=10, height=1, text="reset")
button_reset.config(command=reset)
# TODO #17 Add labelTitle to the grid.
LabelTitle.grid(row=0, columnspan=3)

# TODO #18 Add buttons 0 through 8 to the grid.
button_0.grid(row=1, column=0)
button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=2, column=0)
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=3, column=0)
button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)

root.mainloop()
