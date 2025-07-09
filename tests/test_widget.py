import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_number: str, expected: str) -> None:
    assert mask_account_card(account_number) == expected


@pytest.mark.parametrize(
    "invalid_account",
    ["Maestro 7000792", "VisaPlatinum7000792289606361", "abcdefghijk", "Счет 73654 10843 013587 4305"],
)
def test_mask_invalid_account(invalid_account: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(invalid_account)
        assert str(exc_info)


@pytest.mark.parametrize(
    "data, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-01-29T02:26:18.671407", "29.01.2023"),
        ("2020-10-01T02:26:18.671407", "01.10.2020"),
    ],
)
def test_get_date(data: str, expected: str) -> None:
    assert get_date(data) == expected


@pytest.mark.parametrize(
    "invalid_data", ["2033-01-29T02:26:18.671407", "2023-01-29 02:26:18.671", "abcdefghijk", "1234 5678 9012 3456"]
)
def test_get_date_invalid(invalid_data: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_date(invalid_data)
        assert str(exc_info)


def test_get_date_absent() -> None:
    missing_data = ""
    with pytest.raises(ValueError) as exc_info:
        get_date(missing_data)
        assert str(exc_info)
