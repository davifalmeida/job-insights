from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def data():
    return [
        {"date_posted": "2019-05-08", "max_salary": 10000, "min_salary": 1000},
        {"date_posted": "", "max_salary": 4000, "min_salary": None},
        {"date_posted": "2020-05-08", "max_salary": 1500, "min_salary": 500},
        {"date_posted": "2021-05-08", "max_salary": 500, "min_salary": 100},
    ]


@pytest.fixture
def max_salary(data):
    return [
        data[0],
        data[1],
        data[2],
        data[3]
    ]


@pytest.fixture
def min_salary(data):
    return [
        data[3],
        data[2],
        data[0],
        data[1]
    ]


@pytest.fixture
def date_posted(data):
    return [
        data[3],
        data[2],
        data[0],
        data[1]
    ]


def test_sort_by_criteria(data, max_salary, min_salary, date_posted):
    mock = data.copy()

    sort_by(mock, "max_salary")
    for expected, result in zip(max_salary, mock):
        assert expected == result

    sort_by(mock, "min_salary")
    for expected, result in zip(min_salary, mock):
        assert expected == result

    sort_by(mock, "date_posted")
    for expected, result in zip(date_posted, mock):
        assert expected == result

    with pytest.raises(ValueError, match="invalid sorting criteria: xxx"):
        sort_by(mock, "xxx")
