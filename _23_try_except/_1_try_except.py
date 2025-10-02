def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)


print(find_average(numbers=[1, 2, 3, 4, 5]))  # Output: 3.0
# print(find_average([]))  # Output: ZeroDivisionError: division by zero

try:
    print(find_average(numbers=[]))
except ZeroDivisionError:
    print("The list is empty")

try:
    print(find_average(numbers=[1, 2, 3, 4, 5]))
except ZeroDivisionError:
    print("The list is empty")
