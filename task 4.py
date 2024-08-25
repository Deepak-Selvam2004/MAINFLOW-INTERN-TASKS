#Calculator prgrm
from tkinter import *
from PIL import ImageTk, Image

#Function to initialize the calculator
def init_calculator():
    rt = Tk()
    rt.title("Basic Calculator")
    rt.geometry("600x600")

#Change the path of Background file here
    bg=ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\bg.png')
    bg_label=Label(rt, image=bg)
    bg_label.place(x=0, y=0)

    #Entry Widget
    e=Entry(rt, width=50, justify='center',font=("calibre",14,'normal')) 
    e.grid(row=0, column=0, pady=40,padx=20, columnspan=4)

    #Load images
    images = {
    "1": ImageTk. PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\number-one.png'),
    "2": ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\number-2.png'),
    "3": ImageTk. PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\number-3.png'),
    "4": ImageTk. PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\number-four.png'), 
    "5":ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\number-5.png'),
    "6": ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\six.png'),
    "7": ImageTk. PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\seven.png'),
    "8": ImageTk. PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\number-8.png'),
    "9": ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\number-9.png'),
    "0": ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\zero.png'),
    "C":ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\close.png'),
    "+": ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\plus.png'),
    "-": ImageTk. PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\minus.png'),
    "*": ImageTk. PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\asterisk.png'),
    "/": ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\slash.png'),
    "=": ImageTk.PhotoImage(file='E:\\python codes\\Mainflow internship tasks\\Calculator icons\\equal.png'),
    }
    def button_click(number):
        current=e.get()
        e.delete(0, END) 
        e.insert(0, str(current) + str(number))
    def button_add():
        first_number = e.get()
        global f_num
        global maths
        maths="addition" 
        f_num=float(first_number)
        e.delete(0, END)
    def button_sub():
        first_number= e.get()
        global f_num
        global maths
        maths="subtraction"
        f_num= int(first_number)
        e.delete(0, END)
    def button_div():
        first_number = e.get()
        global f_num
        global maths
        maths="division"
        f_num= int(first_number)
        e.delete(0, END)
    def button_mult(): 
        first_number = e.get()
        global f_num 
        global maths
        maths="multiplication"
        f_num= int(first_number) 
        e.delete(0, END)
    def button_equals():
        second_number = e.get()
        e.delete(0, END)
        if maths=="addition":
            e.insert(0, f_num + int(second_number))
        if maths=="subtraction":
            e.insert(0, f_num - int(second_number)) 
        if maths=="multiplication": 
            e.insert(0, f_num * int(second_number))
        if maths=="division":
            e.insert(0, f_num / int(second_number))
    def button_clear(): 
        e.delete(0, END)
    #Defining Buttons
    buttons={
    "C": (1, 0, button_clear),
    "+": (1, 1, button_add),
    "-": (1, 2, button_sub),
    "*": (1,3, button_mult),
    "1": (2, 0, lambda: button_click(1)),
    "2": (2, 1, lambda: button_click(2)),
    "3": (2, 2, lambda: button_click(3)),
    "/": (2, 3, button_div),
    "4": (3, 0, lambda: button_click(4)),
    "5": (3, 1, lambda: button_click(5)),
    "6": (3, 2, lambda: button_click(6)),
    "=": (3, 3, button_equals),
    "7": (4, 0, lambda: button_click(7)),
    "8": (4, 1, lambda: button_click(8)),
    "9": (4, 2, lambda: button_click(9)),
    "0": (4, 3, lambda: button_click(0)),
    }
    for btn, (row, col, cmd) in buttons.items(): 
        Button(rt, border="3", image=images[btn],command=cmd).grid(row=row, column=col)
    #Keep references to images
    rt.images=images
    rt.mainloop()
#Initialize the calculator
init_calculator()