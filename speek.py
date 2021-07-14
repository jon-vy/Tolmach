import pyttsx3  # Для озвучивания и записи
import os



engine = pyttsx3.init()
ru = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
eng = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# <editor-fold desc="file_name">
def file_name():
    path = f"{os.environ['PYTHONPATH']}\\audio"  # Путь к директории аудио
    file_name = len(os.listdir(path)) + 1  # Количество файлов в этой директории
    print(file_name)

# </editor-fold>
# <editor-fold desc="Функция воспроизведения">
'''Принимает текст, 
скорость воспроизведения,
id голосового движка установленного в системе'''
def sp(txt, rate, lang):
    engine.setProperty('rate', rate)
    engine.setProperty('voice', lang)
    engine.say(txt)
    engine.runAndWait()
# </editor-fold>
# <editor-fold desc="Функция записи текста в mp3">
'''Принимает текст, 
имя файла, 
id голосового движка установленного в системе, 
скорость воспроизведения и'''
def wr(txt, rate, lang, file_lang):
    engine.setProperty('rate', rate)
    engine.setProperty('voice', lang)
    engine.save_to_file(txt, f'audio/{file_lang}_{file_name()}.mp3')
    engine.runAndWait()
# </editor-fold>

if __name__ == "__main__":
    rate = 150
    lang = eng
    txt = 'Stop fucking around! Work hard! Otherwise, you will die a beggar!'
    # file_name = 'test'
    # wr(txt, file_name, lang, rate)
    # sp(txt, rate, lang)
    file_name()