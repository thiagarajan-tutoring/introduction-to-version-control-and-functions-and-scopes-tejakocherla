#!/usr/bin/env python3
""" Contains all code to be written for submission. """

# Do not change this.
global_string = 'This is an example of a global string.'

def reverse_str(s):
    a = ''
    i = len(s)
    while i > 0:
        i = i - 1
        a = a + s[i]
        print(a)
    return a 

    """Reverse the string `s`.

    Args:
        s (str): string to reverse
    Returns:
        a string that is the reverse of s

    Example:
    >>> reverse_str('abc')
    'cba'
    """


def gc_content(s):
    count = 0
    for character in s:
        if character == 's  ':
            count += 1
    return count

    """Calculcates the GC-content for `s`.

    Args:
        s (str): genome sequence (i.e. some ATCG sequence)
    Returns:
        a float, corresponding to the GC-content of `s`

    Example:
    >>> gc_content('GCATGCATTA')
    0.4
    """
   


def sum_list(int_list):
    sum = 0
    i = len(int_list)
    for x in range(0,i):
        sum += int_list[x]
    return sum
    """Sums all entries in `int_list`.

    Args:
        int_list (List[int]): a list of integers
    Returns:
        the sum of all integers in list

    Example:
    >>> sum_list([1, 2, 3, 4])
    10
    """
   


def sum_args(*args):
    print(args)
    sum = 0
    i = len(args) 
    for x in range(0,i):
        sum += args[x]
    return sum
    """Sums all the arguments passed in.

    Args:
        *args: a variable amount of integers
    Returns:
        the sum of all integers passed in via *args

    Example:
    >>> sum_args(1, 2, 3, 4)
    10
    """


def avg_list(int_list):
    sum = 0
    i = len(int_list)
    for x in range(0,i):
        sum += int_list[x]
        sum = sum/i
    return sum
    """Returns the average of integers in `int_list`.

    Args:
        int_list (List[int]): a list of integers

    Returns:
        [float]: the average of all integers in list
    """
    


def one_hot_encoding(num, num_classes=10):
    """Return a list corresponding to the one-hot encoding of `num` for `num_classes` classes.

    Args:
        num (int): the number to one-hot encode
        num_classes (int, optional): The number of classes. Defaults to 10.
    Returns:
        [List[int]]: a list corresponding to the one-hot encoding of `num`

    Note:
        `num` should be less than `num_classes`. If it is not, any output can be returned.

    Example:
    >>> one_hot_encoding(4)
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    >>> one_hot_encoding(3, num_classes=4)
    [0, 0, 0, 1]
    >>> one_hot_encoding(3, 4)
    [0, 0, 0, 1]
    """
    raise NotImplementedError("Delete this once implemented.")


def iterative_fibonacci(n):
    a,b = 0,1
    for i in range (n):
        a,b = b, a+b
    return a
    """Return the `n`-th Fibonacci number using iteration. There should be no recursive calls.

    Args:
        n (int): the index in the Fibonacci sequence to return
    Returns:
        int: the `n`-th Fibonacci number
    Example:
    >>> iterative_fibonacci(5)  # 1, 1, 2, 3, 5
    5
    """
   


def recursive_fibonacci(n):
    if n < 0:
        print("Try another n")
    elif n == 1:
        return 0
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)
    """Return the `n`-th Fibonacci number using recursion. There should be no loops.

    Args:
        n (int): the index in the Fibonacci sequence to return
    Returns:
        int: the `n`-th Fibonacci number
    Example:
    >>> recursive_fibonacci(5)  # 1, 1, 2, 3, 5
    5
    """
   


def binary_search(int_list, k):
    a = 0
    b = len(int_list)-1
    point = False
    while a<=b and not point:
        c = a+b/2
        if int_list[c] == k:
            point = True
            return point
        else:
            return -1
    """Search `int_list` for `k` using binary search. Return -1 if not found.

    You may use iteration or recursion.

    Args:
        int_list (List[int]): Sorted list of integers to search through
        k (int): The value to search for

    Returns:
        int: the index of `k` in `int_list`, or -1 if not found

    Example:
    >>> binary_search([1, 3, 7, 10], 7)
    2
    >>> binary_search([1, 3, 7, 10], 4)
    -1
    """
   


def print_args_info(*args, **kwargs):
    """Print out args and kwargs nicely.

    Args:
        *args: all non-keyword arguments passed in
        **kwargs: all keyword arguments passed in

    Example:
    >>> print_args_info(1, 'asdf', [1, 2, 3], first_kwarg=1, second_kwarg=[3], third_kwarg=None)
    "Args: 1, asdf, [1, 2, 3]. Kwargs: {'first_kwarg': 1, 'second_kwarg': [3], 'third_kwarg': None}
    """
    raise NotImplementedError("Delete this once implemented.")


def set_global_string(s):
    """Get the value of the `global_string` to `s`

    Returns:
        str: the value of `global_string` in the file

    Example:
    >>> from submission import get_global_string
    >>> get_global_string()
    >>> print(global_string)
    'asdf'
    """
    raise NotImplementedError("Delete this once implemented.")

if __name__ == '__main__':
    assert reverse_str('abc') == 'cba'

    #assert gc_content('GCATGCATTA') == 0.4

    assert sum_list([1, 2, 3, 4]) == 10

    assert sum_args(1, 2, 3, 4) == 10

    assert avg_list([1, 2, 3, 4]) == 2.5

    assert one_hot_encoding(4) == [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

    assert iterative_fibonacci(5) == 5

    assert recursive_fibonacci(5) == 5

    assert binary_search([1, 3, 7, 10], 7) == 2
    assert binary_search([1, 3, 7, 10], 4) == -1
    assert binary_search([], 5) == -1

    assert (
        print_args_info(1, 'asdf', [1, 2, 3], first_kwarg=1, second_kwarg=[3]) ==
        """Args: 1, asdf, [1, 2, 3]. Kwargs: {'first_kwarg': 1, 'second_kwarg': [3]}"""
    )

    assert get_global_string() == 'This is an example of a global string.'