from Src.Core.validator import validator
from Src.Core.abstract_model import abstract_reference



###############################################
# Модель организации
class company_model(abstract_reference):
    """
      Модель компании/организации.

      Наследуется от abstract_reference и содержит реквизиты компании для финансовых операций.
      Может инициализироваться данными из настроек приложения.

      Attributes:
          name (str): Название компании (наследуется от abstract_reference)
          inn (int): ИНН (Идентификационный номер налогоплательщика) - 12 символов
          bic (int): БИК (Банковский идентификационный код) - 9 символов
          corr_account (int): Корреспондентский счет - 11 символов
          account (int): Расчетный счет - 11 символов
          ownership (str): Вид собственности - 5 символов
      """

    __inn:int = 0
    __bic:int = 0
    __corr_account:int = 0
    __account:int = 0
    __ownership:str = ""
    def __init__(self, settings):

        if settings.company is not None and validator.validate(settings.company, company_model):
            # Копируем все поля из настроек
            super().__init__(settings.company.name)
            #self.__name = settings.company.name
            self.__inn = settings.company.inn
            self.__bic = settings.company.bic
            self.__corr_account = settings.company.corr_account
            self.__account = settings.company.account
            self.__ownership = settings.company.ownership



    # ИНН
    @property
    def inn(self) -> int:
        return self.__inn
    
    @inn.setter
    def inn(self, value:int):
        validator.validate(value, int, 12)
        self.__inn = value

    # КПП
    @property
    def bic(self) -> int:
        return self.__bic

    @bic.setter
    def bic(self, value:int):
        validator.validate(value, int, 9)
        self.__bic = value

    # Корреспондентский счет
    @property
    def corr_account(self) -> int:
        return self.__corr_account
        
    @corr_account.setter
    def corr_account(self, value:int):
        validator.validate(value, int, 11)
        self.__corr_account = value

    @property
    def account(self) -> int:
        return self.__account
    
    @account.setter
    def account(self, value:int):
        validator.validate(value, int, 11)
        self.__account = value

    @property
    def ownership(self) -> str:
        return self.__ownership
    
    @ownership.setter
    def ownership(self, value:str):
        validator.validate(value, str, 5)
        self.__ownership = value.strip()


       


