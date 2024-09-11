# Function to calculate factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Function to calculate sum of digits of a number
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Input handling: prompt user for a positive integer
num = int(input("Enter a positive integer: "))

# Factorial calculation
factorial_result = factorial(num)
print(f"Factorial of {num} is {factorial_result}")

# Prime check
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Sum of digits
digit_sum = sum_of_digits(num)
print(f"Sum of digits of {num} is {digit_sum}")