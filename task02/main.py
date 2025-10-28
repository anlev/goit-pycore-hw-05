import re
import math
from typing import Callable, Generator, Iterable

def generator_numbers(text: str) -> Generator[float]:
    """
    Yield all valid real numbers found in the given text.
    A number must be an isolated with whitespace on both sides.
    Valid examples: " 1000 ", " 27.45 ", " 324.0 "
    """
    pattern = re.compile(r' \d*\.?\d* ')

    for match in pattern.finditer(text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterable[float]]) -> float:
    """
    Return the sum of all numbers produced by `func(text)`.
    """
    return sum(func(text))


def run_tests():
    text = "Total income: 1000.01 as base income, supplemented by extra 27.45 and 324 dollars."

    nums = list(generator_numbers(text))
    assert nums == [1000.01, 27.45, 324]

    total_income = sum_profit(text, generator_numbers)
    assert math.isclose(total_income, 1351.46)

if __name__ == '__main__':
    run_tests()