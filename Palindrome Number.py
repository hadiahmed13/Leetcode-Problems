def is_palindrome(num: int) -> bool:
    """
    checks to see if the given number is a palindrome.
    >>> is_palindrome(-121)
    False
    >>> is_palindrome(121)
    True
    """

    str_num = str(num)
    reversed_str = str_num[::-1]
    if reversed_str == str_num:
        return True
    return False







