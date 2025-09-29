from Src.Models.nomenclature_group_model import nomenclature_group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model
from Src.settings_manager import settings_manager
from Src.Models.company_model import company_model
import unittest
from Src.Models.storage_model import storage_model
import uuid

class test_models(unittest.TestCase):

    # Провери создание основной модели
    # Данные после создания должны быть пустыми
    def test_empty_createmodel_companymodel(self):
        # Подготовка
        model = company_model()

        # Действие

        # Проверки
        assert model.name == ""


    # Проверить создание основной модели
    # Данные меняем. Данные должны быть
    def test_notEmpty_createmodel_companymodel(self):
        # Подготовка
        model = company_model()
        
        # Действие
        model.name = "test"
        
        # Проверки
        assert model.name != ""

    # Проверить создание основной модели
    # Данные загружаем через json настройки
    def test_load_createmodel_companymodel(self):
        # Подготовка
       file_name = "settings.json"
       manager = settings_manager()
       manager.file_name = file_name
       
       # Действие
       result = manager.load()
            
       # Проверки
       print(manager.file_name)
       assert result == True


    # Проверить создание основной модели
    # Данные загружаем. Проверяем работу Singletone
    def test_loadCombo_createmodel_companymodel(self):
        # Подготовка
        file_name = "./Tst/settings.json"
        manager1 = settings_manager()
        manager1.file_name = file_name
        manager2 = settings_manager()
        check_inn = 123456789
      

        # Действие
        manager1.load()

        # Проверки
        assert manager1.settings == manager2.settings
        print(manager1.file_name)
        assert(manager1.settings.company.inn == check_inn )
        print(f"ИНН {manager1.settings.company.inn}")

    # Проверка на сравнение двух по значению одинаковых моделей
    def test_text_equals_storage_model_create(self):
        # Подготовка
        id = uuid.uuid4().hex
        storage1 = storage_model()
        storage1.id = id
        storage2 = storage_model()   
        storage2.id = id
        # Действие GUID

        # Проверки
        assert storage1 == storage2

    # тестирование создания модели группы номенклатуры
    def test_nomenclature_group_model_create(self):
        # Подготовка
        nomenclature_group = nomenclature_group_model(name="test")
        nomenclature_group.description="test desc"

        assert nomenclature_group.name == "test" and     nomenclature_group.description=="test desc"
    # тестирование создания модели unit и использование
    def test_unit_model(self):
        # Подготовка
        gr=unit_model("gr")
        kg=unit_model("kg",1000,gr)

        mass_g=150000
        mass_kg=150
        assert mass_kg*kg.ratio == mass_g

    # тестирование создания модели номенклатуры с всеми подклассами
    def test_nomenclature_model_create(self):
        # Подготовка
        nomenclature_group = nomenclature_group_model(name="test")

        nomenclature_group.description = "test desc"

        gr = unit_model("gr")
        kg = unit_model("kg", 1000, gr)

        nomenclature=nomenclature_model(name="test nomenclature")
        nomenclature.group=nomenclature_group
        nomenclature.unit=kg

        nomenclature.full_name="t" * 254
        nomenclature.description="test description"
        nomenclature.article="cle"


        assert nomenclature
    # тестирование создания через фаил
    def test_company_model_file_create(self):
        manager = settings_manager()
        manager.file_name="settings.json"
        company = company_model(settings=manager.settings)

        assert company.inn ==123456789

if __name__ == '__main__':
    unittest.main()   
