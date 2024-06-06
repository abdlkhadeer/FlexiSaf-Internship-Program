
def calculate_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum(n - 1)
result = calculate_sum(15)
print("The sum of numbers from 0 to 15 is:", result)