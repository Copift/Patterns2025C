from __future__ import annotations
from Src.Core.abstract_model import abstract_reference
from Src.Core.validator import validator


class unit_model(abstract_reference):
    """
       Модель единицы измерения для системы конвертации величин.

       Представляет собой узел в иерархической системе единиц измерения,
       где каждая единица может быть связана с базовой через коэффициент преобразования.

       Attributes:
           name (str): Наименование единицы измерения (наследуется от AbstractReference).
           ratio (int): Коэффициент преобразования к базовой единице. По умолчанию 1.
           base_model (UnitModel): Ссылка на базовую модель единицы измерения.
                                  Если None, текущая единица считается базовой.

    """
    __ratio: int = 1
    __base_model: unit_model = None

    def __init__(self, name: str, ratio: int = 1, base_model: unit_model = None):
        super().__init__(name)
       # self.__name = name
        self.__ratio = ratio
        self.__base_model = base_model


    #ratio (int): Коэффициент преобразования к базовой единице.
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, value: int):
        self.__ratio = value

    #base_model (UnitModel): Ссылка на базовую модель единицы измерения.
    @property
    def base_model(self) ->  unit_model:
        return self.__base_model

    @ratio.setter
    def ratio(self, value:unit_model):
        self.__base_model = value

