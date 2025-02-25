#---------------- Function to return sum with a default parameter---------------

def sum_numbers(a, b=10):
    return a + b

# Calls the function with only one argument
result1 = sum_numbers(5)
print(f"Result 1: {result1}")

# Calls the function with two argument
result2 = sum_numbers(3,7)
print(f"Result 2: {result2}")

