from Src.Core.validator import validator, argument_exception
from Src.Core.abstract_model import abstract_reference
from Src.Models.company_model import company_model


class storage_model(abstract_reference):
    """
       Модель склада/хранилища.

       Наследуется от abstract_reference и добавляет информацию о местоположении
       и принадлежности к компании.

       Attributes:
           name (str): Название склада (наследуется от abstract_reference)
           address (str): Физический адрес расположения склада
           company (company_model): Компания-владелец склада

    """

    __name: str = ""
    __address: str = ""
    __company: company_model = None


    #   address (str): Физический адрес расположения склада
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str):
        validator.validate(value, str)
        self.__address = value.strip()

    # company (company_model): Компания-владелец склада
    @property
    def company(self) -> company_model:
        return self.__company

    @company.setter
    def company(self, value: company_model):
        validator.validate(value, company_model)
        self.__company = value