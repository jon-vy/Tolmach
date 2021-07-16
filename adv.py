import requests


def adv():
    r = requests.get('http://xn--b1aaibmdhgx7gra.xn--p1ai/adv/tolmach/adv.html')
    if r.status_code == 200:
        ad = r.text % (0, 0, 0)  # в скобках указан цвет текста
    else:
        # ad = '<p style="text-align: center;"><b>Сервер не доступен</b></p>'
        with open('adv.html', "r", encoding="utf-8") as r:
            ad = r.read()
    return ad

if __name__ == "__main__":
    #print(type(adv()))
    print(adv())

