import pyttsx3  # Для озвучивания и записи

# en_txt = 'test record'

engine = pyttsx3.init()
def sp(txt, rate):
    engine.setProperty('rate', rate)
    engine.say(txt)

# engine.save_to_file(en_txt, 'en.mp3')
# engine.save_to_file(ru_txt, 'ru.mp3')
    engine.runAndWait()
if __name__ == "__main__":
    txt = 'тестовая запись'
    rate = 150
    sp(txt, rate)
