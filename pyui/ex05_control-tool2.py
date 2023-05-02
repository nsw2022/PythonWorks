# 컨트롤 도구 - 클래스 사용 생성
from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        Label(frame, text="제목").grid(row=0,column=0)
        Entry(frame).grid(row=0, column=1)
        Button(frame,text="확인").grid(row=0,column=3)

        #체크 박스
        Checkbutton(frame, text="체크 박스 버튼").grid(row=1,column=0)

        # 리스트 목록상자
        listbox = Listbox(frame, height=3, selectmode=SINGLE)
        colors = ['red','green','blue','yellow']
        for item in colors:
                listbox.insert(END, item)
        listbox.grid(row=1,column=1)

root = Tk()
app = App(root)

root.mainloop()
