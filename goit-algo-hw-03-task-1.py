import os
import shutil
import argparse

def copy_and_sort(source_dir, destination_dir):
    try:
        # Перевірка, чи існує вихідна директорія
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' not found.")

        # Перевірка, чи існує директорія призначення, інакше створити її
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Рекурсивно копіюємо та сортуємо файли
        copy_and_sort_recursive(source_dir, destination_dir)

        print("Copying and sorting completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def copy_and_sort_recursive(current_dir, destination_dir):
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)

        if os.path.isdir(item_path):
            # Якщо елемент є директорією, викликаємо функцію рекурсивно
            copy_and_sort_recursive(item_path, destination_dir)
        elif os.path.isfile(item_path):
            # Якщо елемент є файлом, копіюємо його та сортуємо
            copy_and_sort_file(item_path, destination_dir)

def copy_and_sort_file(file_path, destination_dir):
    try:
        # Отримуємо розширення файлу
        _, file_extension = os.path.splitext(file_path)
        file_extension = file_extension[1:]  # Видаляємо крапку з початку розширення

        # Створюємо піддиректорію для розширення, якщо вона не існує
        extension_dir = os.path.join(destination_dir, file_extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)

        # Скопіювати файл у відповідну піддиректорію
        shutil.copy2(file_path, os.path.join(extension_dir, os.path.basename(file_path)))

        print(f"Copied: {file_path} -> {extension_dir}")
    except Exception as e:
        print(f"Error copying file {file_path}: {e}")

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Copy and sort files in a directory.")
    parser.add_argument("source_dir", help="Path to the source directory")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Path to the destination directory (default: dist)")
    args = parser.parse_args()

    # Виклик головної функції з переданими аргументами
    copy_and_sort(args.source_dir, args.destination_dir)

if __name__ == "__main__":
    main()
