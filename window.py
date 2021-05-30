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

        photo = PhotoImage(file='1.png')  # Изменение иконки в левом верхнем
        self.root.iconphoto(False, photo)  # углу окна

        self.frame_1 = Frame(self.root, relief='raised')
        self.frame_1 = LabelFrame()  # Рамка фрейма
        self.frame_1.pack(side=TOP, fill="both", ipady=5, padx=10, pady=5)
        self.label_1 = Label(self.frame_1, text="Настройки", font='Times 12')
        self.label_1.pack(side=LEFT, ipadx=2)

        self.label_2 = Label(self.frame_1, text="Справка", font='Times 12')
        self.label_2.pack(side=LEFT, ipadx=2)
        self.label_3 = Label(self.frame_1, text="Купить", font='Times 12')
        self.label_3.pack(side=LEFT, ipadx=2)

        self.frame_2 = Frame(self.root, relief='raised')
        self.frame_2 = LabelFrame(text="Загрузить из файла")  # Рамка фрейма
        self.frame_2.pack(side=TOP, fill="both", ipady=5, padx=10)

        # Поле выбора файла
        self.path_file = Text(self.frame_2, height=1.1, bg="white", font=("Calibri", 12));
        self.path_file.pack(side=LEFT, padx=10, expand=1, fill=X)
        #self.path_file.insert(0.0, os.getcwd())  # Вставляет путь до родительской папки
        self.path_file.insert(0.0, 'C:\\')

        self.btn_1 = Button(self.frame_2, text="Перевести", command=lambda: self.transl())
        self.btn_1.pack(side=RIGHT, padx=5)

        self.btn_2 = Button(self.frame_2, text="Выбрать файл", command=lambda: self.open_file())
        self.btn_2.pack(side=RIGHT, padx=5)

    def open_file(self):
        #file_name = fd.askopenfilename(title="Выбрать файл", initialdir='/')  # Открывает путь к диску
        #file_name = fd.askopenfilename(title="Выбрать файл", initialdir=os.getcwd())  # Открывает путь к родительской папке
        file_name = fd.askopenfilename(title="Выбрать файл")  # Открывает предыдущий путь
        self.path_file.insert(END, file_name)

    def transl(self):
        pass


    def run(self):
        self.root.mainloop()




if __name__ == "__main__":
    window = Window()
    window.run()

