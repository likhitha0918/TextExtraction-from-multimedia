def print_consecutive_numbers(limit, current=1):
    if current <= limit:
        print(current)
        print_consecutive_numbers(limit, current + 1)

# Example: Print consecutive numbers from 1 to 10
print_consecutive_numbers(10)



