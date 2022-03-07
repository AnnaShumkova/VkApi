# Импортируем нужные модули
import vk, os, time, math
import func
import numpy as np

# Задание 2
# Авторизация
session = vk.Session(access_token='')
vkapi = vk.API(session, v='5.81')


group_1 = np.array(vkapi.groups.getMembers(group_id='hseofficial')['items'])
group_2 = np.array(vkapi.groups.getMembers(group_id='hse')['items'])
general_users = group_1[np.in1d(group_1, group_2)]
print(f"Количесчтво участников состоящих в обоих группах = {len(general_users)}")
print("-"*90)


users_sex = {"m": 0, "w": 0}
users_city = {}
user_info = vkapi.users.get(user_ids=general_users, fields=["city", "sex", "bdate"])
for user in user_info:
    print(f"{user['first_name']} {user['last_name']}")
    # -----------------------------------------------------------
    if user.get('sex') == 1:
        users_sex["w"] = users_sex.get("w") + 1
    else:
        users_sex["m"] = users_sex.get("m") + 1
    # -----------------------------------------------------------
    if user.get('city') is not None:
        city_count = users_city.get(user['city']['title'])
        if city_count is None:
            users_city[(user['city']['title'])] = 1
        else:
            users_city[(user['city']['title'])] = city_count + 1


print("-"*90)

if users_sex.get("w") > users_sex.get("m"):
    print(f"Большая часть подписчиков состоящих в обеих группах: женщины, большинство из них находятся в городе {max(users_city, key=users_city.get)}")
elif users_sex.get("w") < users_sex.get("m"):
    print(f"Большая часть подписчиков состоящих в обеих группах: мужчины, большинство из них находятся в городе {max(users_city, key=users_city.get)}")
else:
    print(f"Количество мужчин и женщин состоящих в обеих группах одинакого, большинство из них находятся в городе {max(users_city, key=users_city.get)}")
