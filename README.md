# pd-diplom-webshop

Дипломная работа к профессии Python-разработчик (Сервис заказа товаров для розничных сетей)

## Описание

Пользователь:
- регистрируется, логинится, выходит
- смотрит список товаров и отдельные товары
- может добавить товары в корзину
- может оформить заказ и посмотреть список заказов

Поставщик:
- может передать админу yaml файл с товарами

Админ:
- загружает товары через специальную команду


## Установка и запуск

- Установите зависимости через requirements.txt
- заимпортируйте файл поставщика через команду `python manage.py loadyaml shop1.yaml`