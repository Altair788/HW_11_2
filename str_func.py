def to_upper_case(value: str) -> str:
    """
    Функция возвращает строку со всеми заглавными буквами.
    Args:
        value: str
    Return:
        str - строка со всеми заглавными буквами.
    """
    return value.upper()


def to_title_case(value: str) -> str:
    """
    Функция возвращает строку с заглавными первыми
    буквами каждого слова в строке.
    Args:
        value: str
    Return:
        str - строка, у которой первые буквы каждого
        слова заглавные.
    """
    return value.title()
