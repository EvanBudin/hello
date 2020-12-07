from tkinter import *
root = Tk()
root.geometry("800x400")
def fuckOff():
    print("Fuck Off")
myEntry = Entry(root, width= 5)
myLabel1 = Label(root, text= "Hello World")
myLabel2 = Label(root, text= "Twinkle Twinkle Asshole")
myButton = Button(width=10,height=4,text= "Press Me", command= fuckOff)
myEntry.grid(row=0,column=0)
myButton.grid(row=3,column=3)
root.mainloop()