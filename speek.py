import pyttsx3  # Для озвучивания и записи

en_txt = 'test Stop fucking around! Work hard! Otherwise, you will die a beggar!'

engine = pyttsx3.init()
def sp(txt, rate, l):
    engine.setProperty('rate', rate)
    engine.setProperty('voice', l)
    engine.say(txt)

# engine.save_to_file(en_txt, 'en.mp3')
# engine.save_to_file(ru_txt, 'ru.mp3')
    engine.runAndWait()
if __name__ == "__main__":
    txt = 'тестовая запись'
    rate = 150
    sp(en_txt, rate)
