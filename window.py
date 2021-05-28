from tkinter import *


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Толмач')
        w = self.root.winfo_screenwidth()  # ширина экрана
        h = self.root.winfo_screenheight()  # высота экрана
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 450  # смещение от середины
        h = h - 350
        self.root.geometry(f'900x600+{w}+{h}')

    def run(self):
        self.root.mainloop()




if __name__ == "__main__":
    window = Window()
    window.run()

