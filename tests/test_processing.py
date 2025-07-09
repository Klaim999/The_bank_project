import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def state() -> list:
    return [{"id": 41428829, "state": "ERROR", "date": "2019-07-03T18:35:29.512364"}]


def test_filter_by_state_key(state: list) -> None:
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(state)
        assert str(exc_info)


@pytest.fixture
def list_result() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_dict() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(list_dict: list, list_result: list) -> None:
    assert filter_by_state(list_dict) == list_result


@pytest.fixture
def list_result_data_true() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_result_data_false() -> list:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_true(list_dict: list, list_result_data_true: list) -> None:
    assert sort_by_date(list_dict, True) == list_result_data_true


def test_sort_by_date_false(list_dict: list, list_result_data_false: list) -> None:
    assert sort_by_date(list_dict, False) == list_result_data_false
