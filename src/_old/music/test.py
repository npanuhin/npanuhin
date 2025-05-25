from requests import post, Session
from fake_useragent import UserAgent

link = "https://passport.yandex.com/auth"
user = UserAgent().random

headers = {
'user-agent': user
}

data = {
    'login': 'npanuhin',
    'passwd': 'D89AyQ5j',
}

session = Session()

responce = session.post(link, headers=headers, data=data)

with open("responce.html", "w") as file:
    file.write(responce.text)
