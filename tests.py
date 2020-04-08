#!/usr/bin/env python3


def test_reverse_str():
    from submission import reverse_str
    assert reverse_str('abc') == 'cba'
    assert reverse_str('') == ''
    assert reverse_str('asdf') == 'fdsa'


def test_gc_content():
    from submission import gc_content
    assert gc_content('GCATGCATTA') == 0.4
    assert gc_content('GCGCGC') == 1.0
    assert gc_content('GCAT') == 0.5


def test_sum_list():
    from submission import sum_list
    assert sum_list([1, 2, 3, 4]) == 10
    assert sum_list([1, 2]) == 3
    assert sum_list([]) == 0


def test_sum_args():
    from submission import sum_args
    assert sum_args(1, 2, 3, 4) == 10
    assert sum_args(1, 2) == 3
    assert sum_args() == 0


def test_avg_list():
    from submission import avg_list
    assert avg_list([1, 2, 3, 4]) == 2.5
    assert avg_list([1, 2]) == 1.5
    assert avg_list([]) == 0.


def test_one_hot_encoding():
    from submission import one_hot_encoding
    assert one_hot_encoding(4) == [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    assert one_hot_encoding(3, num_classes=4) == [0, 0, 0, 1]
    assert one_hot_encoding(3, 4) == [0, 0, 0, 1]


def test_iterative_fibonacci():
    from submission import iterative_fibonacci
    assert iterative_fibonacci(5) == 5
    assert iterative_fibonacci(1) == 1
    assert iterative_fibonacci(2) == 1
    assert iterative_fibonacci(6) == 8


def test_recursive_fibonacci():
    from submission import recursive_fibonacci
    assert recursive_fibonacci(5) == 5
    assert recursive_fibonacci(1) == 1
    assert recursive_fibonacci(2) == 1
    assert recursive_fibonacci(6) == 8


def test_binary_search():
    """
    Example:
    >>> binary_search([1, 3, 7, 10], 7)
    2
    >>> binary_search([1, 3, 7, 10], 4)
    -1
    """
    from submission import binary_search
    assert binary_search([1, 3, 7, 10], 7) == 2
    assert binary_search([1, 3, 7, 10], 4) == -1
    assert binary_search([], 5) == -1


def test_print_args_info():
    from submission import print_args_info
    assert (
        print_args_info(1, 'asdf', [1, 2, 3], first_kwarg=1, second_kwarg=[3]) ==
        """Args: 1, asdf, [1, 2, 3]. Kwargs: {'first_kwarg': 1, 'second_kwarg': [3]}"""
    )


def test_get_global_string():
    from solution import get_global_string
    assert get_global_string() == 'This is an example of a global string.'
