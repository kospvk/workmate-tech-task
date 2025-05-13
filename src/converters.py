def dict_to_dataclass[T](
    data: dict[str, str], cls: type[T], aliases: dict[str, str] | None = None
) -> T:
    """
    Преобразовывает словарь в экземпляр класса T

    :param dict[str, str] data: Словарь с данными для преобразования
    :param type[T] cls: Класс dataclass, в экземпляр которого нужно преобразовать данные
    :param dict[str, str] | None aliases: Словарь алиасов, где ключ - альтернативное имя поля,
        а значение - имя поля в dataclass. Если None, используется прямое совпадение ключей.

    :return: Экземпляр класса cls, заполненный данными из словаря
    :rtype: T

    :raises TypeError: Если переданные данные не соответствуют параметрам конструктора dataclass
    :raises ValueError: Если невозможно преобразовать данные в нужный тип
    """
    aliases = aliases or {}
    init_values = {}
    for key, value in data.items():
        field_name = aliases.get(key, key)
        init_values[field_name] = value
    return cls(**init_values)
