import requests
import config

URL_TRANSLATE = 'https://translate.yandex.net/api/v1.5/tr/translate'

def translate():
    headers_translate = {
    # 'key': 'trnsl.1.1.20180915T102508Z.2c60aa8150729c63.d66d6ee2598a8ba01326ca2d5c874f522f8ab95f',
    'key': config.Api_Key_Yandex,
    'text': 'word',
    'lang': 'en-ru',
    'format': 'plain',
    }

    translate = requests.get(URL_TRANSLATE, params=headers_translate)
    answer = translate.text
    print(f'переведённое слово {answer}')
translate()
print('111')