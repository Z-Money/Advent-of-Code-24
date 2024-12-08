with open("input.txt", "r") as file:
    f = file.read()

safe = 0

def checkLevels(data):
    global safe
    
    if (sorted(data) == data) or (sorted(data, reverse=True) == data):
        for i in range(0, (len(data)-1)):
            level1 = int(data[i])
            level2 = int(data[i+1])
            if 0 < abs(level1 - level2) < 4:
                if i == (len(data)-2):
                    safe += 1
            else:
                break

for line in f.splitlines():
    data = line.split(" ")
    for i in range(0, len(data)):
        data[i] = int(data[i])
    checkLevels(data)

print(safe)