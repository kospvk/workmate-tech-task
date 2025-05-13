import os
from collections.abc import Iterator


def parse_csv_file(
    filename: str, delimiter: str = ",", encoding: str = "utf-8"
) -> Iterator[dict[str, str]]:
    """
    Читает CSV-файл и возвращает генератор словарей, где ключи - заголовки колонок,
    а значения - соответствующие данные строк.

    :param filename: Путь к CSV-файлу.
    :param delimiter: Разделитель колонок в файле (по умолчанию запятая).
    :param encoding: Кодировка файла (по умолчанию 'utf-8').

    :raises ValueError: Если файл не найден или строки имеют неверное количество колонок.

    :return: Генератор словарей с данными из CSV, где ключ - имя колонки, значение - строка из файла.
    """

    if not os.path.exists(filename):
        raise ValueError("Проверьте путь к csv-файлу.")

    with open(filename, encoding=encoding) as f:
        lines = f.readlines()
    if not lines:
        return
    header = lines[0].strip().split(delimiter)
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.strip().split(delimiter)
        yield dict(zip(header, parts))
