"""
    Use below command to unit test your method and docs.
    > python -m doctest -v file.py

"""

from doctest import testmod

def extract_upper(phrase):
    """

    :param phrase:
    :return: list

    >>> extract_upper("This Is Upper")
    ['T', 'I', 'U']
    """
    return list(filter(str.isupper, phrase))

def extract_upper1(phrase):
    """

    :param phrase:
    :return: list

    >>> extract_upper("This Is Upper")
    ['T', 'I', 'U']
    """
    return list(filter(str.isupper, phrase))


if __name__ == "__main__":
    testmod(name="extract_upper1", verbose = True)
    # i = "This Is Upper"
    # print(extract_upper(i))