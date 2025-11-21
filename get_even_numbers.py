def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    Returns a list of even numbers from the given list.

    Args:
        numbers: A list of integers to filter.

    Returns:
        A list containing only the even numbers from the input.

    Example:
        >>> get_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    return [n for n in numbers if n % 2 == 0]


if __name__ == "__main__":
    print(get_even_numbers([1, 2, 3, 4, 5, 6]))
