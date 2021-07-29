import pyttsx3  # Для озвучивания и записи
from pydub import AudioSegment


engine = pyttsx3.init()
ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
eng_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

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
# <editor-fold desc="Функция записи текста в mp3.">
'''Принимает текст, 
имя файла, 
id голосового движка установленного в системе, 
скорость воспроизведения и язык файла'''
def wr(txt, rate, voice_id, lang_file):
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voice_id)
    engine.save_to_file(txt, f'audio/{lang_file}.mp3')
    engine.runAndWait()

# </editor-fold>
# <editor-fold desc="Пауза между ru и eng">
def pause_ru_eng():
    engine.setProperty('rate', 50)
    engine.setProperty('volume', 0)
    engine.save_to_file('Пауза между фразами Пауза между фразами', f'audio/pause.mp3')
    engine.runAndWait()
# </editor-fold>
# <editor-fold desc="Объеденение mp3 файлов">
def concat(file_name):
    sound1 = AudioSegment.from_file("audio/ru.mp3", format="wav")
    sound2 = AudioSegment.from_file("audio/eng.mp3", format="wav")
    pause = AudioSegment.from_file("audio/pause_7_sek.mp3", format="wav")
    sound3 = sound1+pause+sound2
    sound3.export(f"audio/lesson/{file_name}.mp3", format="mp3")
# </editor-fold>
# <editor-fold desc="Добавить паузу в конец mp3">
def add_pause(file_name):
    sound1 = AudioSegment.from_file(f"audio/{file_name}.mp3", format="wav")
    pause = AudioSegment.from_file("audio/pause_12_sek.mp3", format="wav")
    sound3 = sound1 + pause
    sound3.export(f"audio/{file_name}.mp3", format="mp3")
# </editor-fold>


if __name__ == "__main__":
    rate = 150
    lang_file = 'eng'
    txt = 'Stop fucking around! Work hard! Otherwise, you will die a beggar!'
    # file_name = 'test'
    # wr(txt, rate, eng_voice_id, lang_file)
    # sp(txt, rate, lang)
    # file_name()
    pause_ru_eng()
    # concat()