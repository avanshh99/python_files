def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Create a generator object
fib_gen = fibonacci(10)

# Iterate over the generator and print Fibonacci numbers
print("First 10 Fibonacci numbers:")
for num in fib_gen:
    print(num)


# def gen():
#     for i in range(20):
#         yield i

# value=gen()
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
