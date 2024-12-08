with open ("input.txt", "r") as file:
    f = file.read()

list1 = []
list2 = []

for line in f.splitlines():
    data = line.split()
    list1.append(int(data[0]))
    list2.append(int(data[1]))

list1.sort()
list2.sort()

distance = 0
for i in range(0, len(list1)):
    distance += abs(list1[i] - list2[i])

print(distance)

similarity = 0

for i in range(0, len(list1)):
    count = list2.count(list1[i])
    similarity += list1[i] * count

print(similarity)