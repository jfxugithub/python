import tkinter as tk
from tkinter import StringVar

from caseProjects.dictionary.dictionary import translate


def app():
    def show_value():
        val = translate(entry.get())
        text.insert(0.0, val + '\n')  # 插入文本

    def clear_text():
        entry_v.set('')
        text.delete(1.0, tk.END)  # 清空text

    window = tk.Tk()  # 创建窗口
    window.title("英汉词典")  # 设置标题
    window.geometry("500x350+800+300")  # 设置宽500高300,起始坐标(800,300)

    # 单行文本框
    entry_v = StringVar()
    entry_v.set('')
    entry = tk.Entry(window, textvariable=entry_v, width='21', font=('宋体', 15), bg='pink')
    entry.place(x=75, y=20)  # 在window中的坐标

    # Button
    button = tk.Button(window, text='translate', font=('宋体', 10), command=show_value)
    button.place(x=325, y=20)

    frame = tk.Frame()
    # Text
    text = tk.Text(frame, width=30, height='6', bg='white', font=('宋体', 15), foreground='green')
    text.pack(side="left")

    # 滚动条
    scroll = tk.Scrollbar(frame)
    scroll.pack(side="right", fill=tk.Y)

    # 两者的相互关联
    text.config(yscrollcommand=scroll.set)
    scroll.config(command=text.yview)

    frame.place(x=75, y=70)

    clear_button = tk.Button(window, width=45, text='clear', font=('宋体', 10), command=clear_text)
    clear_button.place(x=75, y=265)

    window.mainloop()


app()
