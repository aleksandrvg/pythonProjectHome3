def FindNimber(numbers: list, target: int) -> int:
    for item in numbers:
        if target == item:
            return numbers.index(item)
    return -1

print(FindNimber([2, 4, 6, 8, 10], 6))
print(FindNimber([25, 13, 6, 19, 27, 31], 15))
print(FindNimber([11, 28, 4, 20, 9, 15], 20))
