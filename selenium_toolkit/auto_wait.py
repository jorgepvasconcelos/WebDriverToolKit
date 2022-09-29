import time


class AutoWait:
    __time_to_wait = 0

    @classmethod
    @property
    def wait_time(cls):
        return cls.__time_to_wait

    @classmethod
    def change_wait_time(cls, times: int = 0):
        cls.__time_to_wait = times


def auto_wait(func):
    def wrapper(*args, **kwargs):
        time.sleep(AutoWait.wait_time)
        return func(*args, **kwargs)

    return wrapper
