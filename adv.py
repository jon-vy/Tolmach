import requests

def adv():
    r = requests.get('http://xn--b1aaibmdhgx7gra.xn--p1ai/adv/tolmach/adv.html')
    return r

if __name__ == "__main__":
    ad = adv().text

    print(type(ad))
    print(ad)