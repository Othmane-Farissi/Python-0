def ft_filter(func, iterable):
    """
    Custom implementation of Python's built-in filter() function.

    Applies the given function to each item in the iterable and
    returns a list of items for which the function evaluates to True.

    Args:
        func (callable): A function that takes one argument and returns
        a boolean.
        iterable (iterable): A sequence (list, tuple, etc.) of elements
        to filter.

    Returns:
        list: A list of elements from iterable for which func(element) is True.
    """
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result
