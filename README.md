![foodgram-project-react Workflow Status](https://github.com/AndrewB-V/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master&event=push)
# Продуктовый помощник Foodgram

Проект доступен по адресу https://github.com/AndrewB-V/foodgram-project-react.git

## Описание проекта Foodgram
«Продуктовый помощник»: приложение, на котором пользователи публикуют рецепты, подписываться на публикации других авторов и добавлять рецепты в избранное. Сервис «Список покупок» позволит пользователю создавать список продуктов, которые нужно купить для приготовления выбранных блюд.


- Проект доступен по адресу

```
http://sarmats.ddns.net
http://51.250.80.52
```

_**Дипломная работа выполнена в творческом формате "без рамок"(согласно установок ЯП). Изменения коснулись значительной части стартового проекта включая, но не заканчивая структуру проекта, его наполнения с применением рабочих drf практик и использованием различных фич по сегрегации процессов,удобства их дальнейшего использования, масштабирования и отладки. Сохранены принципы СI и CD. Запуск проекта во всех режимах происходит с минимальным набором мануала.**_


## Запуск проекта через Docker
- В папке infra выполнить команду, что бы собрать контейнер:
```bash
sudo docker-compose up -d --build
```
или

- В корне проекта выполнить команду, что бы собрать контейнер:
```bash
sudo docker-compose -f infra/docker-compose.yml up -d --build
```

_**Дальше ничего делать не надо, все стартует автоматически.**_

- users:
```bash
почта  - vika@vika.ru
пароль - 123qwe!@#

почта  - nik@nik.ru
пароль - 123qwe!@#
```


Автор: [Бондаренко Андрей](https://github.com/AndrewB-V)