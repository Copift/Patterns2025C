from abc import ABC
import uuid
from Src.Core.validator import validator

class abstract_reference(ABC):
    __name:str

    def __init__(self,name:str) -> None:
        super().__init__()
        self.name = name



    """
    Уникальный имя
    """
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        validator.validate(value, str,50)
        self.__name = value.strip()
    


