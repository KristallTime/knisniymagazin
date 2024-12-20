
print("Добро пожаловать в интернет-магазин: Мир книг!")
print("Вы администратор или посетитель?")

#ТОВАРЫ, словарик
goods = {
    "Манга": {"цена": 400, "жанр": "манга", "описание": "Японские комиксы"},
    "Манхва": {"цена": 400, "жанр": "манхва", "описание": "Корейские комиксы"},
    "Мастер и Маргарита": {"цена": 1000, "жанр": "литература", "описание": "Роман Михаила Булгакова"},
    "Война и мир": {"цена": 1050, "жанр": "литература", "описание": "Эпический роман Льва Толстого"},
    "Преступление и наказание": {"цена": 900, "жанр": "литература", "описание": "Роман Федора Достоевского"},
}

#словарики
search_history = {}
purchase_history = {}
carts = {}
users = {}


#следом блоки функций

#показывает товары , жанр и описание
def show_goods(filter=None):
    for name, data in goods.items():
        genre = data.get("жанр")
        description = data.get("описание")
        if filter is None or (genre and filter.lower() in genre.lower()): #фильтрация, манипуляция с текстом. это для того, чтобы
            #все буковки воспринимались . что манга, что МАНГА, все все воспримет. лямбда функция
            print(f"{name}: цена - {data['цена']}, жанр - {genre or 'не указан'}, описание - {description or 'не указано'}")


def add_to_cart(name, product, count):
    if name not in carts:
        carts[name] = {}
    if product in goods: #проверочка,куда без нее(обработка ошибок)
        carts[name][product] = carts[name].get(product, 0) + count
        print(f"{count} x {product} добавлен(ы) в корзину.")
    else:
        print("Товар не найден.")

def show_cart_and_checkout(name):
    if name in carts and carts[name]:
        print("\nТовары в корзине:")
        total_cost = 0
        for product, count in carts[name].items():
            cost = goods[product]["цена"]
            print(f"{count} x {product}: {cost * count}р")
            total_cost += cost * count
        print(f"\nИтоговая стоимость: {total_cost}р")

        while True: # Цикл для проверки ответа пользователя
            answer = input("Купить? (да/нет): ").lower() #проверочка,куда без нее(обработка ошибок)
            if answer in ["да", "нет"]:
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")

        if answer == "да":
            print("Покупка совершена!")
            if name not in purchase_history:
                purchase_history[name] = {}
            purchase_history[name].update(carts[name])
            carts[name] = {}  # Очищаем корзину после покупки
        else:
            print("Покупка отменена.")
    else:
        print("Ваша корзина пуста.")

def update_profile(name):
    if name in users:
        while True:
            print("\nОбновление профиля:")
            print("1. Изменить телефон")
            print("2. Изменить пароль")
            print("3. Вернуться в меню")
            choice = input("Выберите действие: ")
            try:
                choice = int(choice)
                if choice == 1:
                    new_number = input("Введите новый номер телефона: ")
                    users[name]["телефон"] = new_number
                    print("Номер телефона изменен.")
                elif choice == 2:
                    new_password = input("Введите новый пароль: ")
                    users[name]["пароль"] = new_password
                    print("Пароль изменен.")
                elif choice == 3:
                    break
                else:
                    print("Неверный выбор.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
    else:
        print("Пользователь не найден.")

def show_purshare_history(name):
    if name in purchase_history:
        print("Ваша история покупок:")
        for product, count in purchase_history[name].items():
            print(f"{product}: {count} шт.")
    else:
        print("История покупок пуста.")

def add_new_user():

    while True:
        fio = input("Введите ФИО: ")
        if fio:
            break
        print("ФИО не может быть пустым.")

    while True:
        phone = input("Введите номер телефона: ")
        if phone:
            break
        print("Номер телефона не может быть пустым.")

    while True:
        role = input("Введите роль (admin/user): ").lower()
        if role in ["admin", "user"]:
            break
        print("Неверная роль. Выберите 'admin' или 'user'.")

    username = fio.replace(" ", "").lower() # Используем ФИО как username, удаляя пробелы
    if username in users:
        print("Пользователь с таким именем уже существует. Выберите другое имя.")
    else:
      users[username] = {"ФИО": fio, "телефон": phone, "роль": role, "пароль": input("Введите пароль: ")}
      print(f"Пользователь {fio} добавлен.")



while True:
    choice = input("Вы администратор?:\n1. Да\n2. Нет\n: ")
    try:
        choice = int(choice)
        if choice == 1:
            print("Авторизуйтесь, пожалуйста.")

            while True:
                admin_choice = input("Выберите действие:\n1. Зарегистрироваться\n2. Авторизоваться\n: ")
                try:
                    admin_choice = int(admin_choice)
                    if admin_choice == 1:
                        admin_name = input("Введите имя администратора: ")
                        admin_password = input("Введите пароль администратора: ")
                        users[admin_name] = {"пароль": admin_password, "role": "admin"}
                        print(f"Администратор {admin_name} зарегистрирован.")
                        print("Теперь авторизуйтесь:")
                    elif admin_choice == 2:
                        print("Авторизация администратора...")
                        admin_name = input("Введите имя администратора: ")
                        admin_password = input("Введите пароль администратора: ")
                        if admin_name in users and users[admin_name]["пароль"] == admin_password:
                            print("Авторизация успешна!")
                            while True:
                                admin_menu_choice = input(
                                    "Меню администратора:\n"
                                    "1) Просмотр доступных товаров\n"
                                    "2) Добавление данных\n"
                                    "3) Удаление данных\n"
                                    "4) Редактирование данных\n"
                                    "5) Управление пользователями\n"
                                    "6) Добавить нового пользователя\n" # Добавлен пункт меню
                                    "7) Выход\n"
                                    "Ваш выбор: "
                                )
                                try:
                                    admin_menu_choice = int(admin_menu_choice)
                                    if 1 <= admin_menu_choice <= 7:
                                        if admin_menu_choice == 1:
                                            print("Доступные товары:")
                                            for product, data in goods.items():
                                                print(f"{product} ({data['цена']}р)")
                                        elif admin_menu_choice == 2:
                                            new_product = input("Введите название нового товара: ")
                                            while True:
                                                try:
                                                    new_cost = int(input("Введите цену нового productа: "))
                                                    break
                                                except ValueError:
                                                    print("Неверный формат цены. Попробуйте ещё раз.")
                                            goods[new_product] = {"цена": new_cost, "жанр": ""}  # добавляем словарь
                                            print(f"Товар '{new_product}' добавлен.")
                                        elif admin_menu_choice == 3:
                                            product_for_erasing = input("Введите название товара для удаления: ")
                                            if product_for_erasing in goods:
                                                del goods[product_for_erasing]
                                                print(f"Товар '{product_for_erasing}' удален.")
                                            else:
                                                print("Товара не существует.")
                                        elif admin_menu_choice == 4:
                                            product_to_edit = input("Введите название товара для редактирования: ")
                                            if product_to_edit in goods:
                                                new_description = input("Введите новое описание: ")
                                                goods[product_to_edit]["описание"] = new_description
                                                print(f"Описание товара '{product_to_edit}' изменено.")
                                        elif admin_menu_choice == 5:
                                            for username in list(users.keys()):
                                                role = users[username].get('role', 'user')
                                                print(f"Пользователь: {username}, Роль: {role}")
                                                change_role = input(f"Изменить роль пользователя {username}? (да/нет): ").lower()
                                                if change_role == "да":
                                                    while True:
                                                        new_role = input("Введите новую роль (admin/user): ").lower()
                                                        if new_role in ["admin", "user"]:
                                                            users[username]["role"] = new_role
                                                            print(f"Роль пользователя {username} изменена на {new_role}.")
                                                            break
                                                        else:
                                                            print("Неверная роль. Выберите 'admin' или 'user'.")
                                        elif admin_menu_choice == 6:
                                            add_new_user() # Вызов функции добавления нового пользователя
                                        elif admin_menu_choice == 7:
                                            break
                                        else:
                                            print("Неверный выбор. Попробуйте ещё раз.")
                                    else:
                                        print("Неверный выбор. Пожалуйста, введите число от 1 до 7.")
                                except ValueError:
                                    print("Неверный ввод. Введите число от 1 до 7.")
                            break
                        else:
                            print("Неверный логин или пароль.")
                    else:
                        print("Неверный выбор. Пожалуйста, введите 1 или 2.")
                except ValueError:
                    print("Неверный ввод. Введите число 1 или 2.")
            break

        elif choice == 2:
            print("Добро пожаловать, посетитель!")
            name = None
            while True:
                visitor_choice = input("Выберите действие:\n1. Зарегистрироваться\n2. Авторизоваться\n: ")
                try:
                    visitor_choice = int(visitor_choice)
                    if visitor_choice == 1:
                        name = input("Введите ваше имя: ")
                        password = input("Введите ваш пароль: ")
                        users[name] = {"пароль": password, "телефон": "", "role": "user"}  # Ключ "role" добавлен здесь!
                        print(f"Пользователь {name} зарегистрирован.")
                        print("Теперь авторизуйтесь:")
                        purchase_history[name] = {}

                    elif visitor_choice == 2:
                        print("Авторизация...")
                        name_auth = input("Введите ваше имя: ")
                        password_auth = input("Введите ваш пароль: ")
                        if name_auth in users and users[name_auth]["пароль"] == password_auth:
                            name = name_auth  # Устанавливаем имя авторизованного пользователя
                            print("Авторизация успешна!")
                        while True:
                            print("\nМеню:")
                            print("1. Просмотр доступных товаров (с фильтром)")
                            print("2. Добавить товар в корзину")
                            print("3. История покупок")
                            print("4. Просмотр товаров (без фильтра)")
                            print("5. Обновить профиль")
                            print("6. Выйти")

                            visitor_menu_choice = input("Выберите пункт меню: ")

                            try:
                                visitor_menu_choice = int(visitor_menu_choice)
                                if 1 <= visitor_menu_choice <= 6:
                                    if visitor_menu_choice == 1:
                                        while True:
                                            filter = input(
                                                "Фильтр (манга, манхва, литература, или ничего, введите 'выход' для возврата в меню): ")

                                            if filter.lower() == 'выход':
                                                break
                                            show_goods(filter)
                                            if name not in search_history:
                                                search_history[name] = []
                                            search_history[name].extend(list(goods.keys()))
                                    elif visitor_menu_choice == 2:
                                        show_goods()

                                        while True:
                                            leave = False
                                            product_count = input(
                                                "Какой товар и количество хотите купить (например, 'Манга, 2', или 'стоп' для выхода): ")
                                            if product_count.lower() == 'стоп':
                                                break
                                            try:
                                                product, count = product_count.split(',')
                                                add_to_cart(name, product.strip(), int(count.strip()))
                                                while True:
                                                    next_move = input(
                                                        "Хотите ещё преобрести? ('Да', или 'Нет', чтобы купить товары): ")
                                                    if next_move.lower() == 'нет':
                                                        show_cart_and_checkout(name)
                                                        leave = True
                                                        break
                                                    elif next_move.lower() == 'да':
                                                        break
                                                    else:
                                                        print("Неверный ответ. Попробуйте еще раз.")
                                            except ValueError:
                                                print("Неверный формат ввода. Попробуйте еще раз.")
                                            if leave == True:
                                                break

                                    elif visitor_menu_choice == 3:
                                        show_purshare_history(name)
                                    elif visitor_menu_choice == 4:
                                        show_goods()
                                    elif visitor_menu_choice == 5:
                                        update_profile(name)
                                    elif visitor_menu_choice == 6:
                                        show_cart_and_checkout(name)
                                        break  # добавлено для выхода из внутреннего цикла
                                else:
                                    print("Неверный пункт меню.")
                            except ValueError:
                                print("Неверный ввод. Пожалуйста, введите число.")
                            except KeyError:
                                print("Ошибка: пользователь не авторизован")
                        break
                    else:
                        print("Неверный выбор. Попробуйте ещё раз.")


                except ValueError:
                    print("Неверный ввод. Введите число 1 или 2.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите 1 или 2.")

    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число 1 или 2.")
print("Спасибо за посещение!")
