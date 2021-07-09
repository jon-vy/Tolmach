import os
from tkinter import *
from tkinter import filedialog as fd, ttk
from tkhtmlview import HTMLLabel
import sqlite3 as sq
import adv
import speek
import date

HTML = adv.adv().text

class Window:
    def __init__(self):
        # <editor-fold desc="Создание окна">
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
        # </editor-fold>
        # <editor-fold desc="Изменение иконки в левом верхнем">
        photo = PhotoImage(file='img/1.png')  # Изменение иконки в левом верхнем
        self.root.iconphoto(False, photo)  # углу окна
        # </editor-fold>
        # <editor-fold desc="Меню">
        self.mainmenu = Menu(self.root)
        self.root.config(menu=self.mainmenu)
        self.mainmenu.add_command(label='Настройки')
        self.mainmenu.add_command(label='Справка')
        self.mainmenu.add_command(label='Купить')
        # </editor-fold>
        # <editor-fold desc="Загрузить из файла">
        self.frame_2 = Frame(self.root, relief='raised')
        self.frame_2 = LabelFrame(text="Загрузить из файла")  # Рамка фрейма
        self.frame_2.pack(side=TOP, fill="both", ipady=5, padx=10)
        # </editor-fold>
        # <editor-fold desc="Поле выбора файла">
        self.path_file = Text(self.frame_2, height=1.1, bg="white", font=("Calibri", 12))
        self.path_file.pack(side=LEFT, padx=10, expand=1, fill=X)
        self.path_file.insert(0.0, os.getcwd())  # Вставляет путь до родительской папки
        # self.path_file.insert(0.0, 'C:\\')
        # </editor-fold>
        # <editor-fold desc="Кнопка Перевести">
        self.btn_1 = Button(self.frame_2, text="Перевести", command=lambda: self.transl())
        self.btn_1.pack(side=RIGHT, padx=5)
        # </editor-fold>
        # <editor-fold desc="Кнопка Выбрать файл">
        self.btn_2 = Button(self.frame_2, text="Выбрать файл", command=lambda: self.open_file())
        self.btn_2.pack(side=RIGHT, padx=5)
        # </editor-fold>
        # <editor-fold desc="eng txt">
        self.frame_eng = Frame(self.root, relief='raised')
        self.frame_eng = LabelFrame(text="eng txt")  # Рамка фрейма
        self.frame_eng.pack(side=LEFT, expand=1, fill=X, anchor=N)
        self.eng_txt = Text(self.frame_eng, bg="white", width=50, height=15)
        self.eng_txt.insert(0.0, date.select()[0][1])
        self.eng_txt.pack(fill=X)
        # </editor-fold>
        # <editor-fold desc="ru txt">
        self.frame_ru = Frame(self.root, relief='raised')
        self.frame_ru = LabelFrame(text="ru txt")  # Рамка фрейма
        self.frame_ru.pack(side=LEFT, expand=1, fill=X, anchor=N)
        self.ru_txt = Text(self.frame_ru, bg="white", width=50, height=15)
        self.ru_txt.insert(0.0, date.select()[0][2])
        self.ru_txt.pack(fill=X)
        # </editor-fold>
        # <editor-fold desc="Интервал между словами в англ тексте">
        self.eng_word_spacing_frame = Frame(self.root, relief='raised')
        self.eng_word_spacing_frame = LabelFrame(text="Интервал\n между\n словами")
        self.eng_word_spacing_frame.place(x=2, y=320)
        self.eng_word_spacing = Entry(self.eng_word_spacing_frame, width=3, bd=2, font=15, justify=CENTER)
        self.eng_word_spacing.pack(side=LEFT, padx=2, pady=2)
        self.eng_word_spacing_label = Label(self.eng_word_spacing_frame, text="Сек.", justify=LEFT)
        self.eng_word_spacing_label.pack(side=LEFT, padx=2, pady=2)
        # </editor-fold>
        # <editor-fold desc="Выбор голоса англ текст Combobox">
        self.eng_voice_selection_frame = Frame(self.root, relief='raised')
        self.eng_voice_selection_frame = LabelFrame(text="Выбор\nголоса")
        self.eng_voice_selection_frame.place(x=95, y=320)
        self.eng_voice_selection_combo = ttk.Combobox(self.eng_voice_selection_frame,
                                                      values=[
                                                          "Голос 1",
                                                          "Голос 2",
                                                          "Голос 3",
                                                          "Голос 4"
                                                      ])
        self.eng_voice_selection_combo.pack(side=LEFT, padx=2, pady=2)
        # </editor-fold>
        # <editor-fold desc="Скорость воспроизведения в англ тексте">
        self.eng_playback_speed_frame = Frame(self.root, relief='raised')
        self.eng_playback_speed_frame = LabelFrame(text="Скорость\nвоспроизведения")
        self.eng_playback_speed_frame.place(x=135, y=395)
        self.eng_playback_speed = Entry(self.eng_playback_speed_frame, width=3, bd=2, font=15, justify=CENTER)
        self.eng_playback_speed.insert(0, date.select()[0][3])
        self.eng_playback_speed.pack(side=LEFT, padx=2, pady=2)
        # </editor-fold>
        # <editor-fold desc="кнопка воспроизвести в англ тексте">
        self.imagetest = PhotoImage(file="img/play1.png")
        self.eng_play = Button(self.root,
                               cursor="hand2",
                               text="Послушать\nчто\nполучилось",
                               borderwidth=5,
                               relief=GROOVE,
                               image=self.imagetest,
                               compound="right",
                               command=lambda: speek.sp(self.eng_txt.get("1.0", 'end-1c'),
                                                        int(self.eng_playback_speed.get()),
                                                        'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'))
                               #command=lambda: self.s())
        self.eng_play.place(x=2, y=400)
        # </editor-fold>
        # <editor-fold desc="Интервал между словами в ru тексте">
        self.eng_word_spacing_frame = Frame(self.root, relief='raised')
        self.eng_word_spacing_frame = LabelFrame(text="Интервал\n между\n словами")
        self.eng_word_spacing_frame.place(x=824, y=320)
        self.eng_word_spacing = Entry(self.eng_word_spacing_frame, width=3, bd=2, font=15, justify=CENTER)
        self.eng_word_spacing.pack(side=LEFT, padx=2, pady=2)
        self.eng_word_spacing_label = Label(self.eng_word_spacing_frame, text="Сек.", justify=LEFT)
        self.eng_word_spacing_label.pack(side=LEFT, padx=2, pady=2)
        # </editor-fold>
        # <editor-fold desc="Выбор голоса ru текст Combobox">
        self.eng_voice_selection_frame = Frame(self.root, relief='raised')
        self.eng_voice_selection_frame = LabelFrame(text="Выбор\nголоса")
        self.eng_voice_selection_frame.place(x=655, y=320)
        self.eng_voice_selection_combo = ttk.Combobox(self.eng_voice_selection_frame,
                                                      values=[
                                                          "Голос 1",
                                                          "Голос 2",
                                                          "Голос 3",
                                                          "Голос 4"
                                                      ])
        self.eng_voice_selection_combo.pack(side=LEFT, padx=2, pady=2)
        # </editor-fold>
        # <editor-fold desc="Скорость воспроизведения в ru тексте">
        self.ru_playback_speed_frame = Frame(self.root, relief='raised')
        self.ru_playback_speed_frame = LabelFrame(text="Скорость\nвоспроизведения")
        self.ru_playback_speed_frame.place(x=655, y=395)
        self.ru_playback_speed = Entry(self.ru_playback_speed_frame, width=3, bd=2, font=15, justify=CENTER)
        self.ru_playback_speed.insert(0, date.select()[0][4])
        self.ru_playback_speed.pack(side=LEFT, padx=2, pady=2)
        # </editor-fold>
        # <editor-fold desc="кнопка воспроизвести в ru тексте">
        self.image_play_ru = PhotoImage(file="img/play1.png")
        self.ru_play = Button(self.root,
                              cursor="hand2",
                              text="Послушать\nчто\nполучилось",
                              borderwidth=5,
                               relief=GROOVE,
                              image=self.image_play_ru,
                              compound="right",
                              command=lambda: speek.sp(self.ru_txt.get("1.0", 'end-1c'),
                                                       int(self.ru_playback_speed.get()),
                                                       'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'))
        self.ru_play.place(x=767, y=400)
        # </editor-fold>
        # <editor-fold desc="Интервал между ru и eng предложениями">
        self.ru_eng_spacing_frame = Frame(self.root, relief='raised')
        self.ru_eng_spacing_frame = LabelFrame(text="Интервал между\n предложениями ru - eng")
        self.ru_eng_spacing_frame.place(x=375, y=320)
        self.ru_eng_spacing = Entry(self.ru_eng_spacing_frame, width=3, bd=2, font=15, justify=CENTER)
        self.ru_eng_spacing.pack(side=LEFT, padx=2, pady=2)
        self.ru_eng_spacing_label = Label(self.ru_eng_spacing_frame, text="Сек.", justify=LEFT)
        self.ru_eng_spacing.insert(0, date.select()[0][5])
        self.ru_eng_spacing_label.pack(side=LEFT, padx=2, pady=2)
        # </editor-fold>
        # <editor-fold desc="Прослушать всё целиком">
        self.image_play = PhotoImage(file="img/play1.png")
        self.play = Button(self.root,
                              cursor="hand2",
                              text="Послушать\nчто\nполучилось",
                              borderwidth=5,
                              relief=GROOVE,
                              image=self.image_play,
                              compound="right")
        self.play.place(x=385, y=400)
        # </editor-fold>
        # <editor-fold desc="Реклама">
        self.adv_frame = Frame(self.root, relief='raised')
        self.adv_frame = LabelFrame(text="Рекламма")  # Рамка фрейма
        self.adv_frame.place(x=2, y=460)
        self.adv = HTMLLabel(self.adv_frame, html=HTML % (0, 0, 0), width=111, height=6)
        self.adv.pack()
        # </editor-fold>

    '''Функции'''

    # <editor-fold desc="Функция открыть файл">
    def open_file(self):
        file_name = fd.askopenfilename(title="Выбрать файл", filetypes=[("Text files", "*.txt")])  # Открывает предыдущий путь
        self.path_file.delete("0.0", "end")
        self.path_file.insert(END, file_name)
    # </editor-fold>
    # <editor-fold desc="Функция перевода">
    def transl(self):  # Переводчик
        pass
    # </editor-fold>
    # <editor-fold desc="Сохранение данных при закрытии окна">
    def save(self):
        self.eng_t = self.eng_txt.get("1.0", 'end-1c')
        self.ru_t = self.ru_txt.get("1.0", 'end-1c')
        self.eng_playback_sp = self.eng_playback_speed.get()
        self.ru_playback_sp = self.ru_playback_speed.get()
        self.ru_eng_spac = self.ru_eng_spacing.get()
        with sq.connect("db.db") as con:
            self.cur = con.cursor()
            self.cur.execute(f"UPDATE date SET txt_eng = '{self.eng_t}'  WHERE id = 1")
            self.cur.execute(f"UPDATE date SET txt_ru = '{self.ru_t}'  WHERE id = 1")
            self.cur.execute(f"UPDATE date SET eng_playback_speed = '{self.eng_playback_sp}'  WHERE id = 1")
            self.cur.execute(f"UPDATE date SET ru_playback_speed = '{self.ru_playback_sp}'  WHERE id = 1")
            self.cur.execute(f"UPDATE date SET ru_eng_spacing = '{self.ru_eng_spac}'  WHERE id = 1")
            self.root.destroy()
    # </editor-fold>
    # <editor-fold desc="Функция запуска окна">
    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.save)
        self.root.mainloop()
    # </editor-fold>

if __name__ == "__main__":
    w = Window()
    w.run()

