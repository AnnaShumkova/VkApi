# Импортируем нужные модули
from urllib.request import urlretrieve
import vk, os, time, math


def download_album(vkapi, owner_id, album_info):
    album_id = album_info['id']
    album = vkapi.photos.getAlbums(owner_id=owner_id, album_ids=album_id)
    photos_count = album["items"][0]["size"]

    counter = 0  # текущий счетчик
    prog = 0  # процент загруженных
    breaked = 0  # не загружено из-за ошибки
    time_now = time.time()  # время старта

    # Создадим каталоги
    if not os.path.exists('saved'):
        os.mkdir('saved')
    photo_folder = 'saved/album_{0}'.format(album_info['title'])
    if not os.path.exists(photo_folder):
        os.mkdir(photo_folder)

    for j in range(math.ceil(
            photos_count / 1000)):  # Подсчитаем сколько раз нужно получать список фото, так как число получится не целое - округляем в большую сторону
        photos = vkapi.photos.get(owner_id=owner_id, album_id=album_id, count=1000,
                                  offset=j * 1000, photo_sizes=1)  # Получаем список фото

        for photo in photos["items"]:
            counter += 1
            url = photo["sizes"][-1]["url"]  # Получаем адрес изображения
            print(url)
            print('Загружаю фото № {} из {}. Прогресс: {} %'.format(counter, photos_count, prog))
            prog = round(100 / photos_count * counter, 2)
            try:
                urlretrieve(url, photo_folder + "/" + os.path.split(url)[1])  # Загружаем и сохраняем файл
            except Exception:
                print('Произошла ошибка, файл пропущен.')
                breaked += 1
                continue

    time_for_dw = time.time() - time_now
    print(
        "\nВ очереди было {} файлов. Из них удачно загружено {} файлов, {} не удалось загрузить. Затрачено времени: {} сек.".format(
            photos_count, photos_count - breaked, breaked, round(time_for_dw, 1)))
