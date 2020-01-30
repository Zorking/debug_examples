def is_odd(x: int) -> bool:
    return bool(x % 2)


numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if is_odd(numbers[i]):
        del numbers[i]
print(numbers)
