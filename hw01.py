def total_salary(path):
    """
    Calculates the total salary and average salary from a file.

    Args:
        path (str): The path to the file containing salary data.

    Returns:
        tuple: A tuple containing the total salary and average salary.

    Raises:
        FileNotFoundError: If the file specified by the path is not found.
        Exception: If any other error occurs during the calculation.

    """
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  # if line is not empty
                    parts = line.strip().split(',')
                    salary = int(parts[1])
                    total += salary
                    count += 1

        if count == 0:
            return (0, 0)  # If no data is found in the file

        average = total / count
        return (total, average)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)


# Test
total, average = total_salary("./salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")