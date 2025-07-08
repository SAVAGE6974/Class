from tkinter import *

window = Tk()
lbl = Label(window, text="레이블입니다")  # 레이블 생성
btn1 = Button(window, text="One")  # 버튼 생성
btn2 = Button(window, text="Two")  # 두 번째 버튼 생성
lbl.pack()  # 레이블을 창에 추가
btn1.pack(side=LEFT, padx=10)  # 첫 번째 버튼을 창에 추가
btn2.pack(side=LEFT, padx = 10)  # 두 번째 버튼을 창에 추가

window.mainloop()  # 이벤트 루프 시작