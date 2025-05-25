import os

from yandex_music import Client


TOKEN = os.environ.get('TOKEN')
if TOKEN is None:
    with open('token.txt', 'r') as file:
        TOKEN = file.read().strip()

client = Client(TOKEN).init()

print(client.queues_list())
print(client.users_playlists())
