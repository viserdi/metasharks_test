# Тестовое задание Заказ авто

## Как запустить проект
```
- Склонируйте репозиторий
git clone https://github.com/viserdi/metasharks_test.git

- зайдите в директорию проекта metasharks_test, создайте и активируйте виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

- Создайте .env файл в директории проекта (можно скопировать данные из .env.template)
cp .env.template .env

- Перейдите в каталог infra/
cd metasharks_test/infra

- Создайте образы и Соберите контейнеры
docker-compose up

- Выполните миграции, создайте суперюзера, соберите статику 
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input

- при необзодимости заполните базу авто (марки и модели)
docker-compose exec web python manage.py cars_fill_db
```
## Как работает проект:

```
- Откройте страницу в браузере 127.0.0.1
```
```
brand, color, model - Список методов для работы со справочниками
Возможно Создание, Изменение, Чтение и Удаление объектов.

Order - методы работы с Заказами
В методе Post(Put, Patch) использовать id добавляемых объетов

В методе GET(список) параметры:
 ordering - отсортировать по количеству ('count'- по возрастанию, '-count' по убыванию)
 brand - фильтр по Названию Марки авто (по точному совпадению, вводить строку, например BMW)
 page - номер страницы (вывод по 10 заказов на страницу)

count/color - получение списка количества заказанных авто по каждому цвету
count/brand - получение списка количества заказанных авто по каждой марке
```

