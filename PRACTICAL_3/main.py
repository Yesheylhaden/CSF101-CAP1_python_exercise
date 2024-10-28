import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    fibonacci_list = [0, 1]
    for _ in range(2, n + 1):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list[:n + 1]  # Return the list up to the nth Fibonacci number

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

def find_fibonacci_exceeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b
        index += 1
    return index

def is_fibonacci_number(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def fibonacci_ratios(limit):
    ratios = []
    a, b = 0, 1
    for _ in range(limit - 1):
        a, b = b, a + b
        ratios.append(b / a if a != 0 else 0)  # Avoid division by zero
    return ratios

# Testing both functions
n = 30
print("First Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)  # This line is now correct
print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")
print("First 30 Fibonacci numbers (generator):", list(fibonacci_generator(30)))
print("First 30 Fibonacci numbers (memoized):", [fibonacci_memoized(i) for i in range(30)])

value = 100 
index_exceeding_value = find_fibonacci_exceeding(value)
print(f"The first Fibonacci number exceeding {value} is at index {index_exceeding_value}")

number = 21
is_fib = is_fibonacci_number(number)
print(f"Is {number} a Fibonacci number? {'Yes' if is_fib else 'No'}")

ratios = fibonacci_ratios(10)
print("Ratios between consecutive Fibonacci numbers:", ratios)