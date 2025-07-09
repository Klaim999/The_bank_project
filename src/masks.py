def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    if card_number == "":
        raise ValueError("Отсутствует номер карты")
    if len(card_number) != 16:
        raise ValueError("Введён некорректный номер карты")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""

    if account == "":
        raise ValueError("Отсутствует номер счета")
    if len(account) != 20:
        raise ValueError("Введён некорректный номер счета")

    return f"**{account[-4:]}"
