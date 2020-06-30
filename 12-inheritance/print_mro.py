# coding: utf-8


def print_mro(cls):
    """Print the Method Resolution Order of a Class"""
    print(', '.join(c.__name__ for c in cls.__mro__))
