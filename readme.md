#Скрипт по поиску и удалению записей со сетны сообщества VK

##Подготовка:
- установить зависимости:\
`pip install vk_api`\
`pip install python-dotenv`
- создать файл .env в корне проекта и добавить переменные:\
`TOKEN=fdsffadsfedf34324321` токен полученый для Standalone преложения со `scope=wall`\
`GROUP_ID=12345` id сообщества к которому есть права администратора\
`REPEAT_SECONDS=300` таймаут повтора проверки
- заполнить файл `ban.txt` строками которые будем удалять(поиск идет на полное совпадение)
    
##Запуск:
Просто запускаем main.py