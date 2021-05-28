from map import increment


def run_5_times(func):
    def wrapper():
        for i in range(5):
            func()
    return wrapper


def run_N_times(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


def parametrize(arg_names, values_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            args = [elem.strip() for elem in arg_names.split(',')]
            for func_values in values_list:
                parameters = dict(zip(args, func_values))
                func(**parameters)
        return wrapper
    return decorator


@parametrize('value, result', [
    (10, 11), (-7, -6)
])
def test_increment(value, result):
    assert increment(value) == result


@run_5_times
def hello():
    print('Hello!')


@run_N_times(3)
def hello2(username):
    print(f'Hi, {username}!')


if __name__ == '__main__':
    hello2('caiman')
    test_increment(None, None)
