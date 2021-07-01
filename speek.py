# import subprocess

import pyttsx3  # Для озвучивания
# from pydub import AudioSegment
from gtts import gTTS  # Для записи в mp3
from time import sleep

en_txt = 'test record'
ru_txt = 'тестовая запись'

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say(en_txt)
engine.say(ru_txt)
engine.save_to_file(en_txt, 'en.mp3')
engine.save_to_file(ru_txt, 'ru.mp3')
engine.runAndWait()

# subprocess.call(["sox", "in.en.mp3", "in.ru.mp3", "out.mp3"])


# tts = gTTS(text=en_txt, lang='en')
# tts.save('en.mp3')
# tts = gTTS(text=ru_txt, lang='ru')
# tts.save('ru.mp3')
