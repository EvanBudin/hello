import random
from tkinter import *
def reset():
    myList= []
def getBoth():
    counter = 0
    diceAnswer = diceEntry.get()
    typeAnswer = typeEntry.get()
    diceAnswer = int(diceAnswer)
    typeAnswer = int(typeAnswer)
    while counter < diceAnswer:
        myList.append(random.randint(1,typeAnswer))
        counter = counter + 1
    finalAnswer=sum(myList)
    printAnswer= Label(root, text= finalAnswer)
    printAnswer.grid(row=4,column=1)
    endGame= Label(root, text= myList)
    endGame.grid(row=3,column=1)

myList = []
root = Tk()
root.geometry("500x200")
diceEntry= Entry(root, width=20)
typeEntry= Entry(root, width=20)
button= Button(root, width=10,height=5, text="ROLL", command= getBoth)
resetButton= Button(root, width=10,height=5, text="Reset", command= reset)
resetButton.grid(row= 5, column=1)
typeQuestion= Label(root, text="How many sides do these dice have?")
diceQuestion= Label(root, text="How many dice would you like to roll?")
button.grid(row=2,column=1)
typeQuestion.grid(row=0,column=2)
typeEntry.grid(row=1, column=2)
diceEntry.grid(row=1, column=0)
diceQuestion.grid(row=0,column=0)
root.mainloop()