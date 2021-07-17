import pyttsx3  # Для озвучивания и записи
import glob
import os



engine = pyttsx3.init()
ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
eng_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# <editor-fold desc="file_name">
def file_name():
    path = f"{os.environ['PYTHONPATH']}\\audio"  # Путь к директории аудио
    file_name = len(glob.glob(f'{path}\*.mp3')) + 1  # Количество файлов в этой директории
    return file_name

# </editor-fold>

# <editor-fold desc="Функция воспроизведения">
'''Принимает текст, 
скорость воспроизведения,
id голосового движка установленного в системе'''
def sp(txt, rate, voice_id):
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voice_id)
    engine.say(txt)
    engine.runAndWait()
# </editor-fold>

# <editor-fold desc="Функция записи текста в mp3. Так же формирует txt">
'''Принимает текст, 
имя файла, 
id голосового движка установленного в системе, 
скорость воспроизведения и'''
def wr(txt, rate, voice_id, lang_file):
    count = file_name()
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voice_id)
    engine.save_to_file(txt, f'audio/{lang_file}_{count}.mp3')
    engine.runAndWait()
    with open("audio/file.txt", "a") as file:
        file.write(f'{lang_file}_{count}.mp3\n')
# </editor-fold>

# <editor-fold desc="добавляет в список имена файлов">
def write_file_name(name_mp3, lang_file):
    with open("file.txt", "a") as file:
        file.write(f'{name_mp3}.mp3\n')
# </editor-fold>

if __name__ == "__main__":
    rate = 150
    lang_file = 'eng'
    txt = 'Stop fucking around! Work hard! Otherwise, you will die a beggar!'
    # file_name = 'test'
    wr(txt, rate, eng_voice_id, lang_file)
    # sp(txt, rate, lang)
    # file_name()