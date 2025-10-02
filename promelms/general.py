# even_odd
import itertools
from typing import Any, Generator


def even_odd(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


# sum all
def sum_all(numbers: list[int]) -> int:
    return sum(numbers)


# factorial
def calculate_factorial(number: int) -> int:
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


# fibbonacci
def fib(n: int) -> list[int]:
    a = 0
    b = 1
    result = []
    for _ in range(n):
        result.append(a)

        temp_a = b
        temp_b = a + b
        a = temp_a
        b = temp_b
    return result


# palindrome
def palindrome(word: str) -> bool:
    reverse = word[::-1]
    if reverse == word:
        return True
    else:
        return False


# find max
def find_max(numbers: list[int]) -> int:
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


# count words in string
def word_count(words: str) -> dict[str, int]:
    stripped_words = words.split()
    result = dict()
    for word in stripped_words:
        result.update({word: stripped_words.count(word)})
    return result


# count words in string
def word_count_optimized(words: str) -> dict[str, int]:
    stripped_words = words.split()
    result = {}
    for word in stripped_words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

# reverse str
def reverse_string1(word : str) -> str:
    return word[::-1]

def reverse_string2(word: str) -> str:
    result = ""
    for char in word:
        result = char + result
    return result

if __name__ == '__main__':
    print(even_odd(1))
    print(sum_all([1, 2, 3]))
    print(calculate_factorial(5))
    print(fib(5))
    print(palindrome('level'))
    print(find_max([3, 7, 2, 9, 5]))
    print(word_count("hello world hello python"))
    print(word_count_optimized("hello world hello python"))
    print(reverse_string1("python"))