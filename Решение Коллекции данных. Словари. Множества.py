##### Задание №1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
from pprint import pprint
word = []
for i in geo_logs:
    key = i.values()
    for key in i.values():
        for key_2 in range(len(key)):
            if key[key_2] == 'Россия':
                word.append(i)
pprint(word)

#####Задание№2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
unite = ids.values()

my_list = []
for i in unite:
    my_list.extend(i)
my_list2 = set(my_list)
my_list3 = list(my_list2)
print(my_list3)

#####Задача№3
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
statistics = {}
percent = 100 / len(queries)
for x in queries:
    a = len(x.split())
    if a in statistics:
        statistics[a] += 1
    else:
        statistics[a] = 1
for key, value in sorted(statistics.items()):
    percent_2 = round(value * percent)
    print(f"Процент поисковых запросов из {key} слов(а): {percent_2}%, количество запросов: {value}")

#####Задача№4

stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
symbol = sorted(stats.values())

for k in stats:
    if stats[k] == symbol[-1]:
        print(k)
