from tkinter import *

class Window_message:
    def __init__(self, message):
        # <editor-fold desc="Создание окна">
        self.root = Tk()
        self.root.title('Толмач')
        w = self.root.winfo_screenwidth()  # ширина экрана
        h = self.root.winfo_screenheight()  # высота экрана
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 150  # смещение от середины
        h = h - 100
        self.root.geometry(f'300x200+{w}+{h}')
        self.root.resizable(width=False, height=False)  # Минимальный размер окна
        # </editor-fold>

        # <editor-fold desc="сообщение">
        self.frame = Frame(self.root)
        self.message = Label(self.frame, text=message)
        self.frame.pack(expand=True)
        self.message.pack()

        # </editor-fold>

    # <editor-fold desc="Функция запуска окна">
    def run(self):
        self.root.mainloop()
    # </editor-fold>


if __name__ == "__main__":

    w = Window('test')
    w.run()