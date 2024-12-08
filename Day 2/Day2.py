with open("input.txt", "r") as file:
    f = file.read()

results = 0

def checkLevels(data):
    global results
    
    for i in range(0, (len(data)-1)):
        level1 = int(data[i])
        level2 = int(data[i+1])
        if (abs(level1 - level2) < 1) or (abs(level1 - level2) > 3):
            print("Not Safe 1" + str(data))
            return

    if (sorted(data) == data) or (sorted(data, reverse=True) == data):
        results += 1
        print("Safe" + str(data))

    else:
        print("Not Safe 2" + str(data))
            

total = 0
for line in f.splitlines():
    data = line.split(" ")
    checkLevels(data)
    total += 1

print(results)
print(total)