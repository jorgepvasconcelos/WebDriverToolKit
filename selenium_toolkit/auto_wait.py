import time
from random import uniform


class AutoWait:
    __time_to_wait: tuple = (0, 0)

    @classmethod
    @property
    def wait_time(cls) -> tuple:
        return cls.__time_to_wait

    @classmethod
    def change_wait_time(cls, range_time: tuple = (0, 0)):
        if not isinstance(range_time, tuple):
            raise ValueError(f'range_time must be a tuple')

        first, last = range_time

        if not (first >= 0 and last >= first):
            raise ValueError(f'range_time must be a tuple with positive values')

        cls.__time_to_wait = range_time


def auto_wait(func):
    def wrapper(*args, **kwargs):
        range_wait = AutoWait.wait_time

        wait = uniform(*range_wait)
        time.sleep(wait)

        return func(*args, **kwargs)

    return wrapper
