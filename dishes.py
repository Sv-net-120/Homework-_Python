
import pprint



# в файле dishes.txt хранится список блюд: название, ингредиенты и их количество
# Заданеи № 1 :читаем список блюд

def cook_dishes (f):

    cook_book = {}
    for dish_name in f.read().split('\n\n'):
        name, _, *elements = dish_name.split('\n')
        ing_qua_mea = []
        for element in elements:
            ingrdient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, element.split(' | '))
            ing_qua_mea.append({'ingredient_name': ingrdient_name,'quantity': quantity,'measure': measure})
            cook_book[name] = ing_qua_mea
    return (cook_book)

with open('dishes.txt', encoding='utf-8-sig') as f:
    cook_book = cook_dishes(f)
    print('cook_book = ', cook_book, sep='\n')


# Задание № 2: готовим блюда на определенное количество гостей.
def get_shop_list_by_dishes(dishes, persons):

    get_dishes = {}
    for dish in dishes:
        value = cook_book[dish]
        get_persons = []
        for ingred in value:
            for el, el_val in ingred.items():
                if isinstance(el_val,int):
                    el_val *= persons
                    ingred[el] = el_val
                get_persons.append(el_val)
        get_dishes[dish] = get_persons

    return get_dishes

print(get_shop_list_by_dishes(['Омлет', 'Утка по пекински'], 2))

