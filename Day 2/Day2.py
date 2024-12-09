with open("input.txt", "r") as file:
    f = file.read()

safe = 0

def checkLevels(data):
    # Check if the data is sorted in ascending or descending order
    if (sorted(data) == data) or (sorted(data, reverse=True) == data):
        for i in range(0, len(data)-1):
            level1 = int(data[i])
            level2 = int(data[i+1])
            # Check if the difference between consecutive levels is between 1 and 3 (exclusive)
            if 0 < abs(level1 - level2) < 4:
                if i == (len(data)-2):  # Ensure we're at the last element
                    return True
            else:
                return False
    return False

def checkReport(data):
    # First, check if the report is safe without removing any levels
    if checkLevels(data):
        return True
    
    # If the report is unsafe, check if removing one level makes it safe
    for i in range(len(data)):
        modified_data = data[:i] + data[i+1:]
        if checkLevels(modified_data):
            return True
    
    return False

# Main logic to read through the file and check each line
for line in f.splitlines():
    data = line.split(" ")
    data = [int(x) for x in data]  # Convert to integers
    if checkReport(data):
        safe += 1

print("Safe reports count:", safe)