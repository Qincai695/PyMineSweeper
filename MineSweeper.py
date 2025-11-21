"""
扫雷Tkinter版
"""

from tkinter import *
from random import choice

# 初始化Tk根窗口
root = Tk()
root.title("MineSweeper")
# 游戏窗口
# 标题
title_label = Label(root, text="扫雷", font=("宋体", 30), compound=CENTER, width=13)
title_label.grid(column=0, row=0, columnspan=2)


# 定义单元格类
class cell(Button):
    def __init__(self, with_mine=False):
        super().__init__(root, command=self.handle_click, text="     ")
        self.statement = "default"
        self.with_mine = with_mine

    def handle_click(self):
        # handle 点击事件
        if self.with_mine:
            self.statement = "Triggered"
            self.config(text=" 💣 ")
            self.config(background="red", state=DISABLED)
            self.update()
            fail()
        else:
            self.statement = "cleared"
            self.config(background="light gray", state=DISABLED)


def fail():
    # Game over
    pass


def start():
    # 开始游戏
    global game
    game = Toplevel(root)
    game.title("MineSweeper")
    game.protocol("WM_DELETE_WINDOW", game_exit)
    root.withdraw()
    size = int(size_spin.get())
    mine_count = int(mine_spin.get())


def game_exit():
    game.destroy()
    root.deiconify()


def update_range():
    # 随大小数值更改雷数数值
    max_range = int(size_spin.get()) ** 2
    mine_spin.config(to=max_range)


# 菜单界面
start_button = Button(root, text="开始游戏", command=start)
start_button.grid(column=0, row=3, columnspan=2)
exit_button = Button(root, text="退出游戏", command=root.destroy)
exit_button.grid(column=0, row=4, columnspan=2)
item_label = Label(root, text="尺寸: ")
item_label.grid(column=0, row=1, sticky=E)
size_spin = Spinbox(root, from_=2, to=25, command=update_range)
size_spin.grid(column=1, row=1, sticky=S)
mine_label = Label(root, text="雷数: ")
mine_label.grid(column=0, row=2, sticky=E)
mine_spin = Spinbox(root, from_=1, to=1)
mine_spin.grid(column=1, row=2, sticky=S)
update_range()

# 进入消息循环
root.mainloop()
