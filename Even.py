#---------------- Function to check if a number is even------------------

# Returns True if even, False if odd
def is_even_number(n):
    return n % 2 == 0

num=7
result = is_even_number(num)

print("Is the number even?", result)
