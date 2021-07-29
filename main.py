# <editor-fold desc="Импорт модулей">
from win import Window, Window_message  # импортируются все классы из папки win
from protect import updates
# </editor-fold>

'''updates() получает последнее сообщение от сюда t.me/Jon_vy_GuardianBot
Если ничего не получает, то толмач может работать'''
try:
    if updates() == 'Толмач копия 0 доступ разрешён':
        w = Window()
    else:
        w = Window_message(updates())
    w.run()
except:
    w = Window()
    w.run()
