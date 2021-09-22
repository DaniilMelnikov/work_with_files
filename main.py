from pprint import pprint

def convert_to_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name, encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            quantity_ingredient = int(file.readline())
            ingredients_list = []
            for ingredient in range(quantity_ingredient):
                name, quantity, measure = file.readline().split('|')
                ingredients_list.append(
                    {"name": name, "quantity": int(quantity), "measure": measure.strip()}
                )
            result[dish_name] = ingredients_list
            file.readline()
    return result


def get_shop_list_by_dishes(dishes, person_count):
    menu = convert_to_dict('menu.txt')
    order = {}
    list_keys = menu.keys()
    for key in list_keys:
        for dish in dishes:
            if key == dish:
                ingredients_list = menu[key]
                for dict in ingredients_list:
                    for key, value in dict.items():
                        if key == 'name':
                            key_ = value
                            double_dict = {}
                        elif key == 'quantity':
                            if order == {}:
                                double_dict[key] = value * person_count
                            else:
                                for keys in order.keys():
                                    if keys == key_:
                                        double_dict[key] += value
                                        break
                                    else:
                                        double_dict[key] = value * person_count
                        else:
                            double_dict[key] = value
                    order[key_] = double_dict
    return pprint(order)

# get_shop_list_by_dishes(['Утка по-пекински', 'Омлет', 'Чай'], 2)

def file_rotation(file_list, file_result):
    dict_counter = {}
    for file_name in file_list:
        counter = 0
        with open(file_name, encoding='utf-8') as file:
            for line in file:
                counter += 1
            dict_counter[file_name] = counter
    for file_name, lines in sorted_dict(dict_counter).items():
        with open(file_name, encoding='utf-8') as file, open(file_result, 'a', encoding='utf-8') as file_:
                file_.write(f'{file_name}\n')
                file_.write(f'{str(lines)}\n')
                for line in file:
                    file_.write(line)

def sorted_dict(dict):
    sort_dict = {}
    sort_values = sorted(dict.values())
    for value in sort_values:
        for key in dict.keys():
            if dict[key] == value:
                sort_dict[key] = dict[key]
                break
    return sort_dict

file_rotation(['file_1.txt', 'file_2.txt', 'file_3.txt'], 'result_file.txt')