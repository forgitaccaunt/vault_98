<h2 align="center"> ._________________________________.</a> 
<h2 align="center">*/  -                           -  \*</a> 
<h2 align="center">*  -   /  V A U L T - T E K  \   -  *</a> 
<h2 align="center">*  -   \     terminal 98     /   -  *</a> 
<h2 align="center">*\__-___________________________-__/@</a> 
<h2 align="center">        ---------------------</a> 

# Название:

VAULT-TEC TERMINAL 98!

Проект представляет собой "Терминал" компании VAULT-TEC по мотивам серии видеоигр FallOut.
Структура проекта модульная (в будущем будет построена по принципам ООП)
СТруктура БД SQLite3 описана в файле "Databases/structure_db.txt"

Проект разрабатывается в учебных и практических целях, наработки best practices, развития до pet-проекта.


## ОСновные возможности:

 - Авторизация пользователя
     - запрос к БД, получение строки пользователя для дальнейшей работы
 - Игра Случайная цитата
     - получение цитаты путем GET запроса к API
     - ведение счёта (в этой игрей просто испытывал добавление очков)
     - вывод Чемпиона игры и очков текущего пользователя (запрос к БД)
 - Панель управления (доступна пользователям с уровнем доступа ADMIN)
     - проверка прав доступа с помощью запроса к БД
     - добавление и удаление пользователей
     - получения списка пользователей
     - ведение личного журнала (каждый ADMIN отдельно)
     - чтение записей из журнала
     - получение логов действий пользователей
 - Информация о терминале
     - запрос к API для получения IP машины
     - запрос к API для получения геолокации по IP
     - запросы к БД для информации о пользователе
     - чтение из файла "Info/terminal_info.json" другой информации
 - Выход из терминала
     - sys.exit()


## Дополнительные функции:

    - Навигация осуществляется через терминал, всем вводимым с клавиатуры командам прописан .upper()
    - В регистрации нового пользователя используются функции-валидаторы по всем вводимым полям
    - В проекте используются 3 сторонние API
    - Реализовано кеширование результатов некоторых запросов к БД (@lru_cache)
    - Реализовано логирование (настройки в .yaml, запись в .log)


## Функции в разработке:

    - GUI
    - игра ARCADA с графическим интерфейсом
    - чат с другими терминалами (подключение ИИ)
    - поддержка английского интерфейса
    - покрытие тестами
    - развертывание на сервере


## Установка:

    - клонируйте репозиторий
    - запустите файл main.py (в корневом каталоге проекта)
    
## Отзывы и предложения:

Если у Вас есть предложения, пожелания или критика, прошу писать сюда: georgeongit@gmail.com



## Автор

- [@Grigoriy](https://www.github.com/forgitaccaunt)












# vault_98
Для полного функционала используйте:
LOGIN: VISITOR
PASSWORD: IAMADMIN98!   # Включая восклицательный знак

Ограниченный доступ:
LOGIN: AMANDA
PASSWORD: CLOUDY1998


1. Название:
Тестовое название [VAULT-TEK VAULT-98 TERMINAL].


2. Описание:
Проект представляет собой "Терминал" компании VAULT-TEC по мотивам серии видеоигр FallOut.
Структура проекта модульная, функциональная.
СТруктура БД SQLite3 описана в файле "Databases/structure_db.txt"

Проект разрабатывается в учебных и практических целях, наработки best practices, развития до pet-проекта.


3. Основные возможности терминала:
    - Авторизация пользователя
        - запрос к БД, получение строки пользователя для дальнейшей работы
    - Игра Случайная цитата
        - получение цитаты путем GET запроса к API
        - ведение счёта (в этой игрей просто испытывал добавление очков)
        - вывод Чемпиона игры и очков текущего пользователя (запрос к БД)
    - Панель управления (доступна пользователям с уровнем доступа ADMIN)
        - проверка прав доступа с помощью запроса к БД
        - добавление и удаление пользователей
        - получения списка пользователей
        - ведение личного журнала (каждый ADMIN отдельно)
        - чтение записей из журнала
    - Информация о терминале
        - запрос к API для получения IP машины
        - запрос к API для получения геолокации по IP
        - запросы к БД для информации о пользователе
        - чтение из файла "Info/terminal_info.json" другой информации
    - Выход из терминала
        - sys.exit()

Дополнительная информация:
- Навигация осуществляется через терминал, всем вводимым с клавиатуры командам прописан .upper()
- В регистрации нового пользователя используются функции-валидаторы по всем вводимым полям
- В проекте используются 3 сторонние API
- Реализовано кеширование результатов некоторых запросов к БД (@lru_cache)
- Реализовано логирование (настройки в .yaml, запись в .log)


4. Функции в разработке:
    - GUI
    - игра ARCADA с графическим интерфейсом
    - чат с другими терминалами (подключение ИИ)
    - поддержка английского интерфейса

    - логгирование действий пользователей
    - покрытие тестами
    - развертывание на сервере


5. Инструкции по установке / подлючению:
Запуск из файла main.py
(На данном этапе нет необходимости в инструкции по установке / подлючению).


6. Автор:
Григорий Ильзюгенев
TG: @thaigodtattoo
e-mail: georgeongit@gmail.com


Пожелания, критика и вопросы приветствуются.
