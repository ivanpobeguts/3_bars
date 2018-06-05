# Ближайшие бары

Скрипт использует файл с данными о барах Москвы в формате JSON, полученный с сайта [data.mos.ru](https://data.mos.ru/).
Используемые команды:
  * `get_biggest_bar` - получить самый большой бар по количеству мест,
  * `get_smallest_bar` - получить самый маленький бар по количеству мест,
  * `get_closest_bar` - получить ближайший бар. 
  
Для последней команды требуются дополнительные параметры - координаты текущего местоположения пользователя.

# Как запустить
Для работы скрипта требуется скачать JSON файл с данными о барах Москвы. Для этого необходимо:

1. [Зарегистрироваться](https://apidata.mos.ru/Account/Register) на сайте https://apidata.mos.ru для получения API ключа
2. Скачать JSON файл по ссылке https://apidata.mos.ru/v1/features/1796?api_key={Ваш_API_ключ}

Также необходимо:

* Поместить скачанный файл в рабочий каталог и назвать его **bars.json**.
* Установить пакеты из **requirements.txt** командой:

```bash
$ pip install -r requirements.txt
```

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.

Запуск на Linux:

```bash

$ python bars.py get_biggest_bar

{'geometry': {'coordinates': [37.638228501070095, 55.70111462948684], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNu
mber': 2, 'ReleaseNumber': 2, 'RowId': 'fbe6c340-4707-4d74-b7ca-2b84a23bf3a8', 'Attributes': {'global_id': 169375059, 'Name': 'Спорт
 бар «Красная машина»', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Южный административный округ', 'District': 'Дани
ловский район', 'Address': 'Автозаводская улица, дом 23, строение 1', 'PublicPhone': [{'PublicPhone': '(905) 795-15-84'}], 'SeatsCou
nt': 450, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

```

```bash

$ python bars.py get_smallest_bar

{'geometry': {'coordinates': [37.35805920566864, 55.84614475898795], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNum
ber': 2, 'ReleaseNumber': 2, 'RowId': '17adc22c-5c41-4e4b-872f-815b521f2b53', 'Attributes': {'global_id': 20675518, 'Name': 'БАР. СО
КИ', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Северо-Западный административный округ', 'District': 'район Митино'
, 'Address': 'Дубравная улица, дом 34/29', 'PublicPhone': [{'PublicPhone': '(495) 258-94-19'}], 'SeatsCount': 0, 'SocialPrivileges':
 'нет'}}, 'type': 'Feature'}

```

```bash

$ python bars.py get_closest_bar 37.648057 55.760235

{'geometry': {'coordinates': [37.647149354848025, 55.76055272220522], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNu
mber': 2, 'ReleaseNumber': 2, 'RowId': 'aaaa9e46-9b0e-4686-9fb4-891a0accd56f', 'Attributes': {'global_id': 169373538, 'Name': 'Alche
mic ночной клуб', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Центральный административный округ', 'District': 'Басм
анный район', 'Address': 'Чистопрудный бульвар, дом 23, строение 2', 'PublicPhone': [{'PublicPhone': '(903) 724-81-08'}], 'SeatsCoun
t': 80, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
