import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency,expected_ids",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
        ("EUR", []),
        ("GBP", []),
    ],
)
def test_filter_by_currency(transactions, currency, expected_ids):
    result = filter_by_currency(transactions, currency)
    result_list = list(result)

    assert len(result_list) == len(expected_ids)

    assert sorted(tx["id"] for tx in result_list) == sorted(expected_ids)


def test_transaction_descriptions(empty_list):

    assert list(transaction_descriptions([])) == empty_list


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
