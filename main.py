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

result_dict = convert_to_dict('menu.txt')
print(result_dict)