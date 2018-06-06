# Ближайшие бары

Скрипт использует файл с данными о барах Москвы в формате JSON, полученный с сайта [data.mos.ru](https://data.mos.ru/).
Используемые команды:
  * `get_biggest_bar` - получить самый большой бар по количеству мест,
  * `get_smallest_bar` - получить самый маленький бар по количеству мест,
  * `get_closest_bar` - получить ближайший бар. 
  
Для последней команды требуются дополнительные параметры - координаты текущего местоположения пользователя.

# Как запустить
Для работы скрипта требуется:

* Скачать JSON файл с данными о барах Москвы по ссылке https://data.mos.ru/opendata/7710881420-bary .
* Установить пакеты из **requirements.txt** командой:

```bash
$ pip install -r requirements.txt
```

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.

Запуск на Linux:

```bash

$ python bars.py get_biggest_bar

Bar:
{
     "geometry": {
          "coordinates": [
               37.638228501070095,
               55.70111462948684
          ],
          "type": "Point"
     },
     "properties": {
          "Attributes": {
               "Address": "Автозаводская улица, дом 23, строение 1",
               "AdmArea": "Южный административный округ",
               "District": "Даниловский район",
               "IsNetObject": "нет",
               "Name": "Спорт бар «Красная машина»",
               "OperatingCompany": null,
               "PublicPhone": [
                    {
                         "PublicPhone": "(905) 795-15-84"
                    }
               ],
               "SeatsCount": 450,
               "SocialPrivileges": "нет",
               "global_id": 169375059
          },
          "DatasetId": 1796,
          "ReleaseNumber": 2,
          "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8",
          "VersionNumber": 2
     },
     "type": "Feature"
}

```

```bash

$ python bars.py get_smallest_bar

Bar:
{
     "geometry": {
          "coordinates": [
               37.35805920566864,
               55.84614475898795
          ],
          "type": "Point"
     },
     "properties": {
          "Attributes": {
               "Address": "Дубравная улица, дом 34/29",
               "AdmArea": "Северо-Западный административный округ",
               "District": "район Митино",
               "IsNetObject": "нет",
               "Name": "БАР. СОКИ",
               "OperatingCompany": null,
               "PublicPhone": [
                    {
                         "PublicPhone": "(495) 258-94-19"
                    }
               ],
               "SeatsCount": 0,
               "SocialPrivileges": "нет",
               "global_id": 20675518
          },
          "DatasetId": 1796,
          "ReleaseNumber": 2,
          "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53",
          "VersionNumber": 2
     },
     "type": "Feature"
}

```

```bash

$ python bars.py get_closest_bar 37.648057 55.760235

Bar:
{
     "geometry": {
          "coordinates": [
               37.647149354848025,
               55.76055272220522
          ],
          "type": "Point"
     },
     "properties": {
          "Attributes": {
               "Address": "Чистопрудный бульвар, дом 23, строение 2",
               "AdmArea": "Центральный административный округ",
               "District": "Басманный район",
               "IsNetObject": "нет",
               "Name": "Alchemic ночной клуб",
               "OperatingCompany": null,
               "PublicPhone": [
                    {
                         "PublicPhone": "(903) 724-81-08"
                    }
               ],
               "SeatsCount": 80,
               "SocialPrivileges": "нет",
               "global_id": 169373538
          },
          "DatasetId": 1796,
          "ReleaseNumber": 2,
          "RowId": "aaaa9e46-9b0e-4686-9fb4-891a0accd56f",
          "VersionNumber": 2
     },
     "type": "Feature"
}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
