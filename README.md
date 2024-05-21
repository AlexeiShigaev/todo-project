# Список дел (задач)

## Как запустить

Предварительно, убедитесь что у вас установлен docker.


```
git clone https://github.com/AlexeiShigaev/todo-project.git
docker compose up --build
```

## Django admin

Открываем в браузере страницу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
<br>Login: admin; Pass: passqw12

Две модели доступны для добавления/редактирования/удаления данных - это Тэги и Задачи. В Задачах, удерживая Ctrl можно выбрать несколько тэгов

## Swagger документация

Страница [http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger)
