from tkinter import *

window = Tk()

label1 = Label(window, text = "It is Label")
label2 = Label(window, text="문자를", font=("궁서체", 20, "bold"))
label3 = Label(window, text="출력하는", bg = "yellow", bg = "yellow", fg = "red", anchor="w")
label4 = Label(window, text="위젯입니다.", width = 20, height = 3, bg = "skyblue", anchor="se")

label1.pack()
label2.pack()
label3.pack()
label4.pack()

window.mainloop();