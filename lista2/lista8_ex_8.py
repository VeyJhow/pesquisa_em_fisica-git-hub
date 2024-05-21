from numpy import array

array1 = array([0,2,4,6],int)
array2 = array([1,3,5,7],int)

array3 = []

index : int = 0

while index < 4:
    new_number = (array1[index] + array2[index])
    index += 1
    array3.append(new_number)

print(array3)