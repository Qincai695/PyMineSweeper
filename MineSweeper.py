"""
扫雷Tkinter版
"""

from tkinter import *
from random import choice

# 初始化Tk根窗口
root = Tk()
root.title("MineSweeper")
# 游戏窗口
game = Toplevel(root)
game.title("MineSweeper")
# 菜单界面
title_label = Label(root, text="扫雷", font=("宋体", 30), compound=CENTER, width=13)
title_label.grid(column=0, row=0, columnspan=2)
item_label = Label(root, text="尺寸: ")
item_label.grid(column=0, row=1, sticky=E)
size_spin = Spinbox(root, from_=2, to=25)
size_spin.grid(column=1, row=1, sticky=S)
start_button = Button(root, text="开始游戏")
start_button.grid(column=0, row=2, columnspan=2)
# 进入消息循环
root.mainloop()
