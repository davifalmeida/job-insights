from src.pre_built.counter import count_ocurrences
import pytest


def test_counter():

    path = "data/jobs.csv"
    word = "python"
    expected_count = 1639
    assert count_ocurrences(path, word) == expected_count

    with pytest.raises(FileNotFoundError):
        count_ocurrences("path/does/not/exist.csv", "python")
