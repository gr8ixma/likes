import requests
import random

print('''
           Post Likes
/---------------------------------\\

code by : ABDULLAH AL-RUQAISHI
Telegram : @EDISONpy

\---------------------------------/
''')
def LikePost():
    url_post = input('[+]URL Post :').split('?')[0]
    username = input('[+]Username : ')
    print("")
    list = 'qwertyuiopasdfghjklzxcvbnm'
    eml = ''.join(random.choice(list) for i in range(5))
    email = f'{eml}@gmail.com'
    url = 'https://core.poprey.com/api/create_test_order.php'
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-length': '531',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://poprey.com',
    'referer': 'https://poprey.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'x-auth-token': 'null',
    'x-identity-token': 'Iosjvd3fwsF6IjYV6Y4yDkkYUyrRS8WW',
    'x-target-lang': 'en',
    }
    data = {
    'url[0]': url_post,
    'img[0]': 'https://instagram.flwo1-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/177872164_1942348479252659_7240306127772411572_n.jpg?tp=1&_nc_ht=scontent-frx5-1.cdninstagram.com&_nc_cat=111&_nc_ohc=wx3Kyr6tHc0AX_aksZq&edm=ABfd0MgAAAAA&ccb=7-4&oh=e2a94b031bda6a4ab3fa980bc286522a&oe=60A84A33&_nc_sid=7bff83',
    'service': 'Likes',
    'email': email,
    'username': username,
    'system': 'Instagram',
    'plan': '25',
    'tariff': 'gradual',
    'csrf': ''
    }
    req = requests.post(url,headers=headers,data=data)
    print('Request sent ✅. ')
    print("If the likes don't arrive, try again later")
LikePost()