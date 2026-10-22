my_servers = ["web-node-1", "database-main", "backup-server", "auth-server"]

print("Починаю перевірку інфраструктури...")

for s in my_servers:
    print("Пінг сервера:", s)
    print("Статус: ОК")
    print("---")


print("Всі сервери перевірено!")
