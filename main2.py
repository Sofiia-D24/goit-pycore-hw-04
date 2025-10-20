import os
def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    raise ValueError(f"Неправильний формат рядка {line_number}: '{line}'")
                cat_id, name, age_str = parts
                try:
                    age = int(age_str)
                    if age < 0:
                        raise ValueError(f"Вік не може бути від'ємним у рядку {line_number}")
                except ValueError:
                    raise ValueError(f"Неправильний формат віку у рядку {line_number}: '{age_str}'")
                cat_info = {
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age
                }
                cats_list.append(cat_info)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{path}' не знайдено")
    except PermissionError:
        raise PermissionError(f"Немає доступу до файлу '{path}'")
    except Exception as e:
        raise Exception(f"Помилка при читанні файлу '{path}': {str(e)}")
    
    return cats_list


if __name__ == "__main__":
    file_path = os.path.join(os.path.expanduser("~"), "Desktop", "cat.txt")

    try:
        cats = get_cats_info(file_path)
        print("Інформація про котів:")
        print("-" * 40)
        for cat in cats:
            print(f"ID: {cat['id']}")
            print(f"Ім'я: {cat['name']}")
            print(f"Вік: {cat['age']} роки")
            print("-" * 40)
        print("\nТаблиця котів:")
        print(f"{'ID':<24} {'Ім\'я':<10} {'Вік':<3}")
        print("-" * 40)
        for cat in cats:
            print(f"{cat['id']:<24} {cat['name']:<10} {cat['age']:<3}")
    except Exception as e:
        print(f"Помилка: {e}")
