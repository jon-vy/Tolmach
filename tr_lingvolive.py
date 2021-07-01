import requests
import config

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'

def authenticate():
    headers_auth = {'Authorization': 'Basic ' + config.Api_Key_Lingvolive}
    auth = requests.post(URL_AUTH, headers=headers_auth)
    if auth.status_code == 200:
        bearer_token = auth.text
        print(f'bearer_token {bearer_token}')
        return bearer_token

auth_token = authenticate()

def translate(word):
    headers_translate = {
        'Authorization': 'Bearer ' + auth_token
    }
    params = {
            'text': word,
            'srcLang': 1033,
            'dstLang': 1049
        }
    translate = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
    #respons2 = requests.get('https://developers.lingvolive.com/api/v1/Minicard?text=plum&srcLang=1033&dstLang=1049', headers=headrers2)
    answer = translate.text
    print(f'переведённое слово {answer}')


'''header[] = 'Content-length: 0';
$header[] = 'Content-type: application/json';
$header[] = 'Authorization: Basic {Ваш ключ для доступа к API}';'''

