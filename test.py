from datetime import datetime


start_time = datetime.now()
def n_sum(n: str) -> int:
    """Сумма цифр в числе

    Args:
        n (str): Число

    Returns:
        int: Сумма цифр числа
    """
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)

def make_id_number(id: int) -> str:
    """Создает ID покупателяв 7ми значном формате

    Args:
        id (int): ID покупателя

    Returns:
        str: ID в 7значном формате
    """
    max_id_width = 7
    return f'{id:0{max_id_width}}'



def customers_count(n_customers: int)-> dict:
    """Функция создает группы на основе суммы цифр ID пользователей и добавляет пользователей к ним

    Args:
        n_customers (int): количество пользователей
        id (int): стартовый ID равный 0
        groups (dict): словарь групп: ключ - номер группы, значение - количество пользователей
    Returns:
        dict: словарь групп
    """
    id = 0
    groups = {}
    
    for customer in range(n_customers):
        group_number = n_sum(make_id_number(id))
        if group_number not in groups:
            groups[group_number] = 1
        else:
            groups[group_number] += 1
        id += 1
    return groups

def customers_count_with_start_id(n_customers: int, n_first_id: int) -> dict:
    """Функция создает группы на основе суммы цифр ID пользователей и добавляет пользователей к ним

    Args:
        n_customers (int): количество пользователей
        n_first_id (int): стартовый ID
        groups (dict): словарь групп: ключ - номер группы, значение - количество пользователей
    Returns:
        dict: словарь групп
    """
    
    groups = {}
    
    for customer in range(n_customers):
        group_number = n_sum(make_id_number(n_first_id))
        if group_number not in groups:
            groups[group_number] = 1
        else:
            groups[group_number] += 1
        n_first_id += 1
    return groups



if __name__ == "__main__":

    print(customers_count_with_start_id(5000000, 7450001))
    print(datetime.now() - start_time)