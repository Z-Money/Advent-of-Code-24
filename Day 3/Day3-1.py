import re

# Read the input from the file
with open("input.txt", "r") as file:
    data = file.read()

# Regular expressions for matching mul, do, and don't
mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Initialize variables
enabled = True  # At the beginning, mul instructions are enabled
total_sum = 0

# Iterate through the input
i = 0
while i < len(data):
    # Check for a "mul(X,Y)" instruction
    if data[i:i+4] == "mul(":
        i += 4  # Move past "mul("
        start = i
        # Find the first number (X)
        while i < len(data) and data[i] not in [',', ')']:
            i += 1
        num1_str = data[start:i]
        
        # Skip the comma
        if i < len(data) and data[i] == ',':
            i += 1
        
        start = i
        # Find the second number (Y)
        while i < len(data) and data[i] != ')':
            i += 1
        num2_str = data[start:i]
        
        # Process the multiplication if enabled
        if enabled and num1_str.isdigit() and num2_str.isdigit():
            num1 = int(num1_str)
            num2 = int(num2_str)
            total_sum += num1 * num2

    # Check for a "do()" instruction (enables future mul instructions)
    elif data[i:i+4] == "do()":
        enabled = True
        i += 4  # Skip over the "do()"

    # Check for a "don't()" instruction (disables future mul instructions)
    elif data[i:i+7] == "don't()":
        enabled = False
        i += 7  # Skip over the "don't()"

    else:
        i += 1  # Move to the next character if it's not recognized

# Output the result
print(f"The total sum of enabled multiplications is: {total_sum}")