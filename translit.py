import requests
import config
url_auth = 'https://developers.lingvolive.com/api/v1.1/authenticate'
headers_auth = {'Authorization': 'Basic ' + config.ApiKey}
auth = requests.post(url_auth, headers=headers_auth)
bearer_token = auth.text
print(f'bearer_token {bearer_token}')


url_translate = 'https://developers.lingvolive.com/api/v1/Minicard'
headers_translate = {
    'Authorization': 'Bearer ' + bearer_token
}
params = {
        'text': 'word',
        'srcLang': 1033,
        'dstLang': 1049
    }
translate = requests.get(url_translate, headers=headers_translate, params=params)
#respons2 = requests.get('https://developers.lingvolive.com/api/v1/Minicard?text=plum&srcLang=1033&dstLang=1049', headers=headrers2)
answer = translate.text
print(f'переведённое слово {answer}')


'''header[] = 'Content-length: 0';
$header[] = 'Content-type: application/json';
$header[] = 'Authorization: Basic {Ваш ключ для доступа к API}';'''

