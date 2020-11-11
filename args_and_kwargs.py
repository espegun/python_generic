def func1(a, b):
    """
    Accepts unnamed positional arguments, named arguments
    and unnamed
    """
    print(a, b)


def func2(**kwargs):
    """
    Accepts both named arguments and a unnamed **dictionary.
    The results is in any case the dictionary kwargs inside
    the function.
    A useful application is to pass down kwargs until it hits
    a function with named arguments.
    """

    print(f"kwargs is a dict inside the function: {kwargs}")


d = {"a": "Hello", "b": "World"}


func1(**d)  # Hello World

func2(a="Goodbye", b="cruel world")  # kwargs is a dict: {'a': 'Goodbye', 'b': 'cruel world'}
func2(**d)  # kwargs is a dict: {'a': 'Hello', 'b': 'World'}
func2(d)  # TypeError


