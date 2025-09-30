from Src.Core.abstract_model import abstract_reference
from Src.Core.validator import validator, argument_exception
from Src.Models.nomenclature_group_model import nomenclature_group_model
from Src.Models.unit_model import unit_model


class nomenclature_model(abstract_reference):
    """
      Модель номенклатуры товара/продукта.

      Наследуется от abstract_reference и содержит полную информацию о товаре,
      включая артикул, группу и единицу измерения.

      Attributes:
          name (str): Краткое название номенклатуры (наследуется от abstract_reference)
          full_name (str): Полное наименование номенклатуры
          article (str): Артикул товара
          group (nomenclature_group_model): Группа номенклатуры
          unit (unit_model): Единица измерения товара


      """
    __full_name: str = ""
    __article: str = ""
    __group: nomenclature_group_model = None
    __unit: unit_model = None

   #full_name (str): Полное наименование номенклатуры
    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value:str):
        validator.validate(value, str, 255)
        self.__full_name = value

    #article (str): Артикул товара
    @property
    def article(self) -> str:
        return self.__article

    @article.setter
    def article(self, value: str):
        validator.validate(value, str, 10)
        self.__article = value.strip()

    #group (nomenclature_group_model): Группа номенклатуры
    @property
    def group(self) -> nomenclature_group_model:
        return self.__group

    @group.setter
    def group(self, value: nomenclature_group_model):
        if value and not isinstance(value, nomenclature_group_model):
            raise argument_exception("Группа должна быть объектом nomenclature_group_model")
        self.__group = value

    #unit (unit_model): Единица измерения товара
    @property
    def unit(self) -> unit_model:
        return self.__unit

    @unit.setter
    def unit(self, value: unit_model):
        if value and not isinstance(value, unit_model):
            raise argument_exception("Единица измерения должна быть объектом unit_model")
        self.__unit = value
