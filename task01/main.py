from typing import Callable, Dict

def caching_fibonacci() -> Callable[[int], int]:
    cache: Dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0

        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def run_tests():
    fib = caching_fibonacci()
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(15) == 610
    assert fib(20) == 6765


if __name__ == '__main__':
    run_tests()
