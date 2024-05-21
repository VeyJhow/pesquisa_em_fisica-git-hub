list1 = [1,2,3]
list2 = [4,5,6]

index : int = 0

while index < 3:
    list1.append(list2[index])
    index += 1

print(list1)