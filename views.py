import json
import datetime

FILE = 'data.json'



def get_data(filter=None):
    with open(FILE) as file: 
        data = json.load(file)
    if filter:
        filter_type = input('Как вы хотите сортировать ?: по цене или по статусу : ').lower() 
    
        if filter_type == 'по цене': 
            price = float(input('Введите цену: '))
            cost = input(f'Вы хотите товар больше или меньше чем {price}? : ').lower()
            if cost == 'больше':
                new_data = [i for i in data if i['price'] >= price]
                if new_data:
                    return new_data
                return 'Нет такого продукта'
            elif cost == 'меньше':
                new_data = [i for i in data if i['price'] <= price]
                if new_data:
                    return new_data
                return 'Нет такого продукта'

        if filter_type == 'по статусу':
            is_active = input('Хотите получить активные или не активные? ')
            if is_active == 'активные': 
                new_data = [i for i in data if i['is_active'] == True]
                if new_data: 
                    return new_data
            elif is_active == 'не активные': 
                new_data = [i for i in data if i['is_active'] == False]
                return new_data
    return data


def get_products(): 
    with open(FILE) as file:
        data = json.load(file)
        return data


def get_product(id): 
    data = get_data()
    product = [i for i in data if i['id'] == id]
    if product: 
        return product[0]
    return 'Нет такого продукта'


def post_prouct(): 
    data = get_data()
    max_id = max([i['id'] for i in data])
    data.append  ({
        'id' : max_id + 1, 
        'name' : input('Введите название нового товара:  '),
        'price' : float(input('Введите цуну нового товара: ')),
        'created_at' : str(datetime.datetime.now()),
        'description' : input('Введите описание: '),
        'update_at' : str(datetime.datetime.now()),
        'is_active' : True
    })
    with open(FILE, 'w') as file: 
        json.dump(data, file)
        return 'Вы успешно опубликовали продукт'


def update_product(id):
    data = get_data()
    update_product = [i for i in data if i['id'] == id]
    if update_product:
        update_product = data.index(update_product[0])
        data[update_product]['name'] = input('Введите новое имя:  ')
        data[update_product]['price'] = float(input('Введите новую цену: '))
        data[update_product]['update_at'] = str(datetime.datetime.now())
        data[update_product]['description'] = input('Введите новое описание: ')
        data[update_product]['is_active'] = False if input('Актуален ли товар? Да/нет ').lower()=="нет" else True         
        json.dump(data, open(FILE, 'w'))
        return 'Вы успешно обновили продукт'
    return 'Нет такого продукта'


def delete_product(id): 
    data = get_data()
    delete_product = [i for i in data if i['id'] == id]
    if delete_product: 
        data.remove(delete_product[0])

        json.dump(data, open(FILE, 'w'))
        return 'Вы успешно удалили товар'
    return 'Нет такого товара'

