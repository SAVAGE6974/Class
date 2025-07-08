from tkinter import *

def print_1():
    lab1["text"] = "첫 번째 버튼 클릭"
def print_2():
    btn2["text"] = "두 번째 버튼 클릭"

window = Tk()

lab1 = Label(window, text="레이블 입니다")
btn1 = Button(window, text="One", command=print_1)
btn2 = Button(window, text="Two", command=print_2)

lab1.pack()
btn1.pack()
btn2.pack()

window.mainloop()