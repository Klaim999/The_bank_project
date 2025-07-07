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


list_cs = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(sort_by_date(list_cs, False))
