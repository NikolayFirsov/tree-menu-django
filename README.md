# Древовидное Меню на Django
Проект представляет собой простое Django приложение, которое реализует древовидное меню.
Проект разработан с использованием Django и Python 3.12.

## Установка и запуск проекта
### Создание виртуального окружения и установка зависимостей
Перед началом работы убедитесь, что у вас установлен Python 3.12. Далее выполните следующие шаги:
1. Клонируйте репозиторий проекта.
2. Создайте виртуальное окружение:
    ```
    python3.12 -m venv venv
    ```
3. Активируйте виртуальное окружение:
   - Для Windows:
       ```
       venv\Scripts\activate
       ```
   - Для MacOS/Linux:
       ```
       source venv/bin/activate
       ```
    Перейдите в папку с проектом:
       ```
       cd menu_project/
       ```
5. Установите все зависимости:
    ```
    pip install -r requirements.txt
    ```

### Применение миграций и создание суперпользователя
После установки зависимостей, выполните миграции для настройки базы данных:
1. Примените миграции:
    ```
    python manage.py migrate
    ```
    При выполнении миграций автоматически создаются два дефолтных меню.
    Первое меню `named_url_menu` с использованием именных url'ов такой иерархии: 
    ```
    - Для клиентов
    -- О нас
    -- Контакты
    -- Отзывы
    ```
    Второе меню `direct_link_menu` с использованием прямых url'ов такой иерархии: 
    ```
    - Тема 1
    -- Страница 1.1
    -- Страница 1.2
    --- Страница 1.2.1
    - Тема 2
    -- Страница 2.1
    -- Страница 2.2
    ```
    Эти пункты меню появятся в базе данных и будут доступны в интерфейсе. 
    По умолчанию в проекте будет использоваться только одно меню `direct_link_menu`
2. Создайте суперпользователя для доступа к административной панели:
    ```
    python manage.py createsuperuser
    ```
   Следуйте инструкциям для создания учетной записи администратора.

### Запуск проекта
Запустите встроенный сервер разработки Django:
```
python manage.py runserver
```
Сервер будет доступен по адресу: http://127.0.0.1:8000
На главной странице будет отображаться древовидное меню `direct_link_menu`, через которое можно переходить на различные разделы сайта.
>В проект добавлен простой мидлвар для подсчета и вывода в консоль количество запросов к БД, одно меню = один запрос

## Добавление нового меню на страницу
Чтобы добавить еще одно меню на страницу, выполните следующие шаги:
1. В административной панели Django создайте новое меню. Для этого перейдите в админку http://127.0.0.1:8000/admin/
    Войдите под учетной записью суперпользователя и в разделе Menus создайте новый объект меню с нужными пунктами.
2. В шаблоне base.html добавьте новое меню с нужным названием:
    ```html
    <nav class="menu">
            <h3>Меню</h3>
            {% draw_menu 'direct_link_menu' %}<!-- direct_link_menu это название меню -->
            <!-- можно вставить еще одно меню как в строке выше, но с другим названием -->
            <!-- {% draw_menu 'named_url_menu' %}  для проверки меню с именнованным урлами-->
        </nav>
    ```
    Теперь на странице будут отображаться два отдельных меню.

### Заключение
Этот проект — хороший пример реализации динамических древовидных меню с помощью Django. 
Для отрисовки одного меню используется всего один запрос к БД.
Вы можете расширить функционал, добавив новые меню через административную панель и выводя их в нужных шаблонах.
