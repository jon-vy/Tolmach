import os
from tkinter import *
from tkinter import filedialog as fd


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
        self.root.minsize(900, 600)  # Минимальный размер окна

        photo = PhotoImage(file='1.png')  # Изменение иконки в левом верхнем
        self.root.iconphoto(False, photo)  # углу окна

        # Меню
        self.mainmenu = Menu(self.root)
        self.root.config(menu=self.mainmenu)
        self.mainmenu.add_command(label='Настройки')
        self.mainmenu.add_command(label='Справка')
        self.mainmenu.add_command(label='Купить')

        # Загрузить из файла
        self.frame_2 = Frame(self.root, relief='raised')
        self.frame_2 = LabelFrame(text="Загрузить из файла")  # Рамка фрейма
        self.frame_2.pack(side=TOP, fill="both", ipady=5, padx=10)

        # Поле выбора файла
        self.path_file = Text(self.frame_2, height=1.1, bg="white", font=("Calibri", 12));
        self.path_file.pack(side=LEFT, padx=10, expand=1, fill=X)
        self.path_file.insert(0.0, os.getcwd())  # Вставляет путь до родительской папки
        # self.path_file.insert(0.0, 'C:\\')

        self.btn_1 = Button(self.frame_2, text="Перевести", command=lambda: self.transl())
        self.btn_1.pack(side=RIGHT, padx=5)

        self.btn_2 = Button(self.frame_2, text="Выбрать файл", command=lambda: self.open_file())
        self.btn_2.pack(side=RIGHT, padx=5)

        # eng txt
        self.frame_eng = Frame(self.root, relief='raised')
        self.frame_eng = LabelFrame(text="eng txt")  # Рамка фрейма
        self.frame_eng.pack(side=LEFT,  expand=1, fill=X, anchor=N)
        self.eng_txt = Text(self.frame_eng, bg="white", width=50, height=15)
        self.eng_txt.pack(fill=X)
        self.w = Entry(self.frame_eng, width=3, bd=2, font=15, justify=CENTER)
        self.w.pack(side=LEFT, padx=5, pady=10)

        # ru txt
        self.frame_ru = Frame(self.root, relief='raised')
        self.frame_ru = LabelFrame(text="ru txt")  # Рамка фрейма
        self.frame_ru.pack(side=LEFT,  expand=1, fill=X, anchor=N)
        self.ru_txt = Text(self.frame_ru, bg="white", width=50, height=15)
        self.ru_txt.pack(fill=X)





    def open_file(self):  # Открыть файл
        file_name = fd.askopenfilename(title="Выбрать файл", filetypes=[("Text files", "*.txt")])  # Открывает предыдущий путь
        self.path_file.delete("0.0", "end")
        self.path_file.insert(END, file_name)

    def transl(self):  # Переводчик
        pass


    def run(self):  # Запуск окна
        self.root.mainloop()




if __name__ == "__main__":
    w = Window()
    w.run()

