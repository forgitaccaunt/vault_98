
<h2 align="center">
 
 ![](https://i.pinimg.com/564x/67/dc/8b/67dc8bea96a682b4251b42b1f9a5cd89.jpg)
</a> 


# Название: VAULT-TEC TERMINAL 98!

Проект представляет собой "Терминал" компании VAULT-TEC по мотивам серии видеоигр FallOut.
Структура проекта модульная (в будущем будет построена по принципам ООП).
Структура БД SQLite3 описана в файле "Databases/structure_db.txt".

Проект разрабатывается в учебных и практических целях, наработки best practices, развития до pet-проекта.


## Оcновные возможности:

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


### Дополнительные функции:

    - Навигация осуществляется через терминал, всем вводимым с клавиатуры командам прописан .upper()
    - В регистрации нового пользователя используются функции-валидаторы по всем вводимым полям
    - В проекте используются 3 сторонние API
    - Реализовано кеширование результатов некоторых запросов к БД (@lru_cache)
    - Реализовано логирование (настройки в .yaml, запись в .log)


### Функции в разработке:

    - GUI
    - игра ARCADA с графическим интерфейсом
    - чат с другими терминалами (подключение ИИ)
    - поддержка английского интерфейса
    - покрытие тестами
    - развертывание на сервере


## Установка:

    - клонируйте репозиторий
    - запустите файл main.py (в корневом каталоге проекта)

    
Для полного функционала используйте:

LOGIN: VISITOR
PASSWORD: IAMADMIN98!   # Включая восклицательный знак

Ограниченный доступ:

LOGIN: AMANDA
PASSWORD: CLOUDY1998
    
## Отзывы и предложения:

Если у Вас есть предложения, пожелания или критика, прошу писать сюда: georgeongit@gmail.com



## Автор
- Григорий Ильзюгенев
- [@Grigoriy](https://www.github.com/forgitaccaunt)
- georgeongit@gmail.com
- TG: @thaigodtattoo
