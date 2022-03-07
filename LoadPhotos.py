# Импортируем нужные модули
import vk, os, time, math
import func


# Авторизация
session = vk.Session(access_token='token')
vkapi = vk.API(session, v='5.81')

# Задание 1
url = "https://vk.com/album-132_47581240"
# Разбираем ссылку
owner_id = url.split('/')[-1].split('_')[0].replace('album', '')

album_list = vkapi.photos.getAlbums(owner_id=owner_id)

for album in album_list['items']:
    print(album)
    # Функция дла загрузки файла была вынесена в отдельный файл func.py
    func.download_album(vkapi, owner_id, album)


