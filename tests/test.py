from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

card_number = "7000792289606361"

print(get_mask_card_number(card_number))

account = "73654108430135874305"

print(get_mask_account(account))

account = "Visa Classic 6831982476737658"

print(mask_account_card(account))

data = "2024-03-11T02:26:18.671407"

print(get_date(data))
