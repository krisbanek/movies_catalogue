import pytest

def get_fibonacci_number(n):
    if n == 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b

@pytest.mark.parametrize('n, result', (
   (0, 0),
   (1, 1),
   (2, 1),
   (3, 2),
   (10, 55),
   (15, 610)
))
def test_fibonacci(n, result):
   assert get_fibonacci_number(n) == result