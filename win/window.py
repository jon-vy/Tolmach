import os
from tkinter import *
from tkinter import filedialog as fd, ttk
a = 1

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
        self.root.resizable(width=False, height=False)  # Минимальный размер окна

        photo = PhotoImage(file='img/1.png')  # Изменение иконки в левом верхнем
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

        # ru txt
        self.frame_ru = Frame(self.root, relief='raised')
        self.frame_ru = LabelFrame(text="ru txt")  # Рамка фрейма
        self.frame_ru.pack(side=LEFT,  expand=1, fill=X, anchor=N)
        self.ru_txt = Text(self.frame_ru, bg="white", width=50, height=15)
        self.ru_txt.pack(fill=X)










        # Интервал между словами в англ тексте
        self.eng_word_spacing_frame = Frame(self.root, relief='raised')
        self.eng_word_spacing_frame = LabelFrame(text="Интервал\n между\n словами")
        self.eng_word_spacing_frame.place(x=2, y=320)
        self.eng_word_spacing = Entry(self.eng_word_spacing_frame, width=3, bd=2, font=15, justify=CENTER)
        self.eng_word_spacing.pack(side=LEFT, padx=2, pady=2)
        self.eng_word_spacing_label = Label(self.eng_word_spacing_frame, text="Сек.", justify=LEFT)
        self.eng_word_spacing_label.pack(side=LEFT, padx=2, pady=2)

        # Выбор голоса англ текст
        self.eng_voice_selection_frame = Frame(self.root, relief='raised')
        self.eng_voice_selection_frame = LabelFrame(text="Выбор\nголоса")
        self.eng_voice_selection_frame.place(x=95, y=320)
        # self.eng_voice_selection = Entry(self.eng_voice_selection_frame, width=3, bd=2, font=15, justify=CENTER)
        # self.eng_voice_selection.pack(side=LEFT, padx=2, pady=2)
        self.eng_voice_selection_combo = ttk.Combobox(self.eng_voice_selection_frame,
                                                      values=[
                                                          "Голос 1",
                                                          "Голос 2",
                                                          "Голос 3",
                                                          "Голос 4"
                                                      ])
        self.eng_voice_selection_combo.pack(side=LEFT, padx=2, pady=2)

        # Скорость воспроизведения в англ тексте
        self.eng_playback_speed_frame = Frame(self.root, relief='raised')
        self.eng_playback_speed_frame = LabelFrame(text="Скорость\nвоспроизведения")
        self.eng_playback_speed_frame.place(x=135, y=395)
        self.eng_playback_speed = Entry(self.eng_playback_speed_frame, width=3, bd=2, font=15, justify=CENTER)
        self.eng_playback_speed.pack(side=LEFT, padx=2, pady=2)

        # кнопка воспроизвести в англ тексте
        self.imagetest = PhotoImage(file="img/play1.png")
        self.eng_play = Button(self.root, cursor="hand2", text="Послушать\nчто\nполучилось", borderwidth=5, relief=GROOVE, image=self.imagetest, compound="right")
        self.eng_play.place(x=2, y=400)









        # Интервал между словами в ru тексте
        self.eng_word_spacing_frame = Frame(self.root, relief='raised')
        self.eng_word_spacing_frame = LabelFrame(text="Интервал\n между\n словами")
        self.eng_word_spacing_frame.place(x=824, y=320)
        self.eng_word_spacing = Entry(self.eng_word_spacing_frame, width=3, bd=2, font=15, justify=CENTER)
        self.eng_word_spacing.pack(side=LEFT, padx=2, pady=2)
        self.eng_word_spacing_label = Label(self.eng_word_spacing_frame, text="Сек.", justify=LEFT)
        self.eng_word_spacing_label.pack(side=LEFT, padx=2, pady=2)

        # Выбор голоса ru текст
        self.eng_voice_selection_frame = Frame(self.root, relief='raised')
        self.eng_voice_selection_frame = LabelFrame(text="Выбор\nголоса")
        self.eng_voice_selection_frame.place(x=655, y=320)
        # self.eng_voice_selection = Entry(self.eng_voice_selection_frame, width=3, bd=2, font=15, justify=CENTER)
        # self.eng_voice_selection.pack(side=LEFT, padx=2, pady=2)
        self.eng_voice_selection_combo = ttk.Combobox(self.eng_voice_selection_frame,
                                                      values=[
                                                          "Голос 1",
                                                          "Голос 2",
                                                          "Голос 3",
                                                          "Голос 4"
                                                      ])
        self.eng_voice_selection_combo.pack(side=LEFT, padx=2, pady=2)

        # Скорость воспроизведения в ru тексте
        self.eng_playback_speed_frame = Frame(self.root, relief='raised')
        self.eng_playback_speed_frame = LabelFrame(text="Скорость\nвоспроизведения")
        self.eng_playback_speed_frame.place(x=655, y=395)
        self.eng_playback_speed = Entry(self.eng_playback_speed_frame, width=3, bd=2, font=15, justify=CENTER)
        self.eng_playback_speed.pack(side=LEFT, padx=2, pady=2)

        # кнопка воспроизвести в ru тексте
        self.image_play_ru = PhotoImage(file="img/play1.png")
        self.eng_play = Button(self.root, cursor="hand2", text="Послушать\nчто\nполучилось", borderwidth=5,
                               relief=GROOVE, image=self.image_play_ru, compound="right")
        self.eng_play.place(x=767, y=400)




















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

