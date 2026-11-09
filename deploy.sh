#!/bin/bash

echo "Починаємо автоматичне розгортання сервера"
sudo docker run -d -p 8080:80 nginx
echo "Сервер Nginx успішно запущено у фоновому режимі"
echo "Поточний статус контейнерів:"
sudo docker ps
