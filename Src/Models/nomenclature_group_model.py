from Src.Core.abstract_model import abstract_reference
from Src.Core.validator import validator


class nomenclature_group_model(abstract_reference):
    """
    Модель группы номенклатуры.

    Наследуется от abstract_reference и добавляет описание для группы товаров/продуктов.

    Attributes:
        name (str): Название группы номенклатуры (наследуется от abstract_reference)
        description (str): Описание группы номенклатуры


    """
    __description: str = ""


    # description (str): Описание группы номенклатуры
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        validator.validate(value, str)
        self.__description = value.strip()
