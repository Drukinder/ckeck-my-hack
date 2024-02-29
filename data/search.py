COLOR_CODE = {
    "RESET": "\033[0m",
    "GREEN": "\033[32m",
    "RED": "\033[31m",
    "BOLD": "\033[01m"
}

def get_number(database_file, search_value):
    found = False
    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
            phone = data[7]
            if search_value in phone:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]  
                municipal_education = data[18]  
                institution_name = data[20]  

                print(f'''{COLOR_CODE["GREEN"]}
╔══════                                                   ══════╗
║                                                               ║
		{COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}База: school.mos.ru
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}ID пользователя: {data[0]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Дата регистрации: {data[1]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Фамилия: {data[2]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Имя: {data[3]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Отчество: {data[4]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Дата рождения: {data[5]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Пол: {data[6]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Телефон: {data[7]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Почта: {data[8]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Роль: {data[9]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Класс: {data[13]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Адрес: {data[19]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Страна: {data[16]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Гражданство: {data[15]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Регион: {data[17]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Муниципальное образование: {data[18]}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]} Наименование учреждения: {data[20]}

║                                                               ║
╚══════                                                   ══════╝
                ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR] {COLOR_CODE["GREEN"]}Ничего не найдено в базе данных школ, продолжаю поиск...{COLOR_CODE["RESET"]}')

def get_yandex_eda_number(database_file, search_value):
    found = False
    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 5:
            phone = data[0]
            if search_value in phone:
                first_name = data[1]
                full_name = data[2]
                email = data[3]
                address_info = data[4].split(',')

                address_city = address_info[0]
                address_street = address_info[1]
                address_house = address_info[2]
                address_entrance = address_info[3]

                print(f'''{COLOR_CODE["GREEN"]}
╔══════                                                   ══════╗
║                                                               ║
		{COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}База: Яндекс.Еда
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Телефон: {phone}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Имя: {first_name}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Полное имя: {full_name}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Электронная почта: {email}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Город: {address_city}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Улица: {address_street}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Дом: {address_house}
                {COLOR_CODE["RED"]}[+]{COLOR_CODE["GREEN"]}Подъезд: {address_entrance}

║                                                               ║
╚══════                                                   ══════╝
                ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["RED"]}[ERROR] {COLOR_CODE["GREEN"]}Ничего не найдено в базе данных по номеру телефона, извини :(.{COLOR_CODE["RESET"]}')
