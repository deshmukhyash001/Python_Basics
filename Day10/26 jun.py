def hello_world():
    return "Hello, World!"

def add_numbers(a, b):
    return a + b

def square_number(n):
    return n * n

def is_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def max_of_three(a, b, c):
    return max(a, b, c)

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

def reverse_string(s):
    return s[::-1]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def area_of_circle(radius, pi=3.14159):
    return pi * radius * radius

def sum_list(lst):
    return sum(lst)

def second_largest(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return None
    unique.remove(max(unique))
    return max(unique)

def remove_duplicates(lst):
    return list(set(lst))

def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def main():

    hello_world()
    add_numbers(2, 3)
    square_number(4)
    is_even_or_odd(5)
    max_of_three(4, 9, 2)
    factorial(5)
    is_prime(7)
    fibonacci_series(5)
    is_palindrome("radar")
    count_vowels("hello world")
    reverse_string("Python")
    gcd(12, 15)
    lcm(4, 6)
    area_of_circle(3)
    sum_list([1, 2, 3])
    second_largest([1, 5, 3, 4])
    remove_duplicates([1, 2, 2, 3])
    even_numbers([1, 2, 3, 4, 5, 6])
    celsius_to_fahrenheit(0)
    sort_list([3, 1, 4, 2])


if __name__ == '__main__':
    main()
