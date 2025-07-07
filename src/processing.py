def filter_by_state(list_dict: list, state_key: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    соответствует указанному значению.
    """
    new_list_dict = []
    for dict_ in list_dict:

        if dict_["state"] not in ["EXECUTED", "CANCELED"]:
            raise ValueError("Некорректные статус")

        if dict_["state"] == state_key:
            new_list_dict.append(dict_)

    return new_list_dict


def sort_by_date(dict_list: list, reverse: bool) -> list:
    """Функция, которая сортирует дату по заданному параметру"""
    return sorted(dict_list, key=lambda x: x["date"], reverse=reverse)



