import abc
from typing import Any, Iterable

from models import Employee


class Report(abc.ABC):
    """
    Абстрактный базовый класс для отчетов.

    Определяет интерфейс для генерации отчета на основе
    итерируемой коллекции объектов Employee.
    """

    @abc.abstractmethod
    def generate(self, employees: Iterable[Employee]) -> Any:
        """
        Генерирует отчет по списку сотрудников.

        :param employees: Итерация по объектам Employee.
        :return: Результат отчета в произвольном формате.
        """
        pass
