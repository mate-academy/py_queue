import pytest

import queue


def test_push_pop():
    q = queue.Queue(5)
    q.push(1)
    assert q.pop() == 1


def test_double_push_pop():
    q = queue.Queue(5)
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    assert q.pop() == 2


def test_empty():
    q = queue.Queue(5)
    with pytest.raises(IndexError):
        assert q.pop()


def test_full():
    q = queue.Queue(5)
    for i in range(5):
        q.push(i)
    with pytest.raises(IndexError):
        q.push(1)


def test_length():
    q = queue.Queue()
    for i in range(5):
        q.push(1)
    for i in range(3):
        assert q.pop() == 1
    for i in range(3):
        q.push(2)
    for i in range(3):
        assert q.pop() == 2
    for i in range(2):
        assert q.pop() == 1

