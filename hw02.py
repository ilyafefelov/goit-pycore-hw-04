def get_cats_info(path):
    """
    Reads a file containing cat information and returns a list of dictionaries
    representing each cat's information.

    Args:
        path (str): The path to the file containing cat information.

    Returns:
        list: A list of dictionaries, where each dictionary represents a cat's information.
            Each dictionary contains the following keys: 'id', 'name', and 'age'.

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: If any other error occurs while reading the file.

    """
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:  # Перевірка, що рядок містить достатньо частин
                    cat_dict = {
                        'id': parts[0],
                        'name': parts[1],
                        'age': parts[2]
                    }
                    cats_info.append(cat_dict)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    return cats_info

# Test
cats_info = get_cats_info("cats.txt")
for cat in sorted(cats_info, key=lambda x: int(x['age'])):
    print(cat)