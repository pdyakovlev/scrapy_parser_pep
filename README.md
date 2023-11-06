## Описание

Скрапер [scrapy_parser_pep] собирает документы PEP с ресурса [https://peps.python.org/](https://peps.python.org/) и формирует результат двух типов:

* pep_{datetime}.csv - список всех PEP (номер, название и статус)
* status_summary_{datetime}.csv - сводка по статусам PEP, сколько найдено документов в каждом статусе (статус, количество)

## Развернуть локально

Склонировать проект, создать виртуальное окружение и проинициализировать зависимости:

```bash
cd scrapy_parser_pep
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Парсер запускается из root-директории проекта командой

```bash
scrapy crawl pep
```