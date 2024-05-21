list1 = [1,3,5,7,9]
list2 = [0,2,4,6,8]

list3 = []

index : int = 0

while index < 5:
    new_number = (list1[index] + list2[index])
    index += 1
    list3.append(new_number)

print(list3)
