from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""

    list_data = account_card.split()
    count = -1
    for data_card in list_data:

        count += 1
    if count <= -1:
        raise ValueError("Информация отсутствует")
    if count <= 0 or count >= 3:
        raise ValueError("Некорректная информация")

    if len(list_data[count]) == 16:
        mask = get_mask_card_number(list_data[count])
    else:
        mask = get_mask_account(list_data[count])
    if count == 2:
        result = f"{list_data[0]} {list_data[1]} {mask}"
    else:
        result = f"{list_data[0]} {mask}"

    return result


def get_date(date: str) -> str:
    """Функция, которая изменяет формат даты"""

    if date == "":
        raise ValueError("Данные отсутствуют")
    if len(date) != 26 or date[:3] != "202":
        raise ValueError("Некорректные данные")

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
