import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("2200710030856270", "2200 71** **** 6270"),
        ("4421347815610413", "4421 34** **** 0413"),
        ("5112093597523751", "5112 09** **** 3751"),
    ],
)
def test_get_mask_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card", ["220071003080", "44213478156104131234", "abcdefghijk", "1234 5678 9012 3456"]
)
def test_get_mask_invalid_number(invalid_card: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_card)
        assert str(exc_info)


def test_get_mask_card_absent() -> None:
    missing_nuber = ""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(missing_nuber)
        assert str(exc_info)


@pytest.mark.parametrize(
    "account_number, expected",
    [("40702810068696817220", "**7220"), ("40702810112346728272", "**8272"), ("40702810932310508462", "**8462")],
)
def test_get_mask_number_account(account_number: str, expected:str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "invalid_account", ["4070281006869681", "407028100686968172204741", "abcdefghijk", "40702 8100686968 17220"]
)
def test_get_mask_invalid_account(invalid_account:str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(invalid_account)
        assert str(exc_info)


def test_get_mask_account_absent() ->None:
    account_nuber = ""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_nuber)
        assert str(exc_info)
