# NOTE
# When a func gets passed into
# a decorator it looses its attributes
# __name__
# __doc__
# __module__

# SOLUTION
# use the @wraps decorator from functools
# to preserve these attributes

from functools import wraps

def simple_decorator(func):
    @wraps(func)
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper


@simple_decorator
def foo(x):
    """function(x) -> print"""
    print("What is up - x {}".format(x))

if __name__ == "__main__":
    foo("Hi")
    print("foo-names {}".format(foo.__name__))
    print("doc string".format(foo.__doc__))

