def is_odd(x: int) -> bool:
    return bool(x % 2)


numbers = [n for n in range(10)]
numbers[:] = [n for n in numbers if not is_odd(n)]
print(numbers)
