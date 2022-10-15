import json
import os

from cars.models import Brand, CarModel


JSON_PATH = 'cars/management/json'


def load_from_json(file):
    with open(os.path.join(JSON_PATH, file + '.json'),
              'r', encoding='utf-8') as infile:
        return json.load(infile)


def fill():
    print('Загружаем базу автомобилей...')

    cars_dict = load_from_json('cars').get('list')

    for brand, model_list in cars_dict.items():
        new_brand = Brand.objects.create(name=brand)
        for model in model_list:
            CarModel.objects.create(brand=new_brand, name=model)
    print('Готово!')
