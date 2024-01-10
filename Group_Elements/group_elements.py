list1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
list2 = []
index = 0

for i in range(len(list1[0])):
    list2.append([])
    for j in range(len(list1)):
        list2[index].append(list1[j][index])
    index = index + 1

a, b, c = list2[0], list2[1], list2[2]
print(a, b, c)
