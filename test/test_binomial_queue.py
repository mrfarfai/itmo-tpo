import pytest
from src.binomial_queue import BinomialQueue

def make_queue(values):
    q = BinomialQueue()
    for v in values:
        q.insert(v)
    return q

def extract_all(q):
    result = []
    try:
        while True:
            result.append(q.delete_min())
    except ValueError:
        pass
    return result


@pytest.mark.parametrize(
    "values, expected_first",
    [
        ([5, 3, 8, 1], 1),
        ([42], 42),
    ],
)
def test_insert_and_first(values, expected_first):
    q = make_queue(values)
    assert q.delete_min() == expected_first


@pytest.mark.parametrize(
    "values, expected_seq",
    [
        ([5, 3, 8, 1], [1, 3, 5, 8]),
        ([3, 1, 2], [1, 2, 3]),
    ],
)
def test_sequential_delete(values, expected_seq):
    q = make_queue(values)
    assert extract_all(q) == expected_seq


@pytest.mark.parametrize(
    "vals1, vals2, expected_seq",
    [
        ([5, 10], [3, 7], [3, 5, 7, 10]),
        ([2, 4], [1, 3], [1, 2, 3, 4]),
    ],
)
def test_merge(vals1, vals2, expected_seq):
    q1 = make_queue(vals1)
    q2 = make_queue(vals2)
    q1.merge(q2)
    assert extract_all(q1) == expected_seq


def test_empty_queue_raises():
    q = BinomialQueue()
    with pytest.raises(ValueError):
        q.delete_min()
