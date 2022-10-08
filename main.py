from views import *

def main(): 
    while True: 
        print('Здравствуйте, вот наш функционал: \n1 - Получить все товары \n2 - Получить определенный товар \n3 - опубликовать товар \n4 - удалить товар \n5 - обновить товар\n 0 - Выйти')

        method_ = int(input('Выберайте: '))
        if method_ == 1: 
            filter = True if input('Хотите отфильтровать? ').lower() == 'да' else False 
            print(get_data(filter))

        elif method_ == 2: 
            print(get_product(int(input('Введите id продукта: '))))
        elif method_ == 3: 
            print(post_prouct())
        elif method_ == 4: 
            print(delete_product(int(input('Введите id продукта: '))))
        elif method_ == 5: 
            print(update_product(int(input('Введите id продукта'))))
        elif method_ == 0: 
            break
        else: 
            print('Нет такого метода Попробуйте еще')

if __name__ == '__main__':
    main()
