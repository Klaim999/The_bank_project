def filter_by_currency(list_transactions, currency):
    """Функция которая, фильтрует транзакции по заданной валюте"""

    return (
        transaction
        for transaction in list_transactions
        if transaction["operationAmount"]["currency"]["code"] == currency
    )


def transaction_descriptions(list_transactions):
    """Функция которая, возвращает описание каждой операции по очереди"""

    for transaction in list_transactions:
        yield transaction["description"]


def card_number_generator(numbers_start, numbers_stop):
    """Функция которая, генерирует номера карт в заданном диапазоне"""

    for number in range(numbers_start, numbers_stop + 1):
        card_num = f"{number:016d}"
        formatted_number = " ".join([card_num[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_number
