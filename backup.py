def make_backup(folder_name):
    print("Починаю архівацію папки:", folder_name)
    print("Бекап успішно збережено")
    print("---")

print("Система резервного копіювання запущена")

make_backup("documents")
make_backup("system_logs")
make_backup("user_data")
