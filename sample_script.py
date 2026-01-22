def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

data = [10, 20, 30, 40]
print("Average:", calculate_average(data))
