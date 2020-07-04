def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('Inside decorator')
        func(*args, **kwargs)
    return wrap_func

@my_decorator
def test_function(*args, **kwargs):
    print('Inside test function ' + args[0])
    print('Inside test function ' + kwargs.get('one'))


def main():
    test_function('hello', 'hi', 'namaste', one='hi', two="hello")

if __name__ == '__main__':
    main()
