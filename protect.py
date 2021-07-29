import requests
import config

API_link = f"https://api.telegram.org/bot{config.TELEGR_TOKEN}/"

def updates():
    r = requests.get(f"{API_link}getUpdates?offset=-1").json()

    message = r['result'][0]['message']['text']
    return message

if __name__ == "__main__":
    print(updates())