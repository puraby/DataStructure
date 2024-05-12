def insertionSort(intList):
     n = len(intList)
     for i in range(1, n):
        k = i
        while (k > 0) and (intList[k-1] < intList[k]):
           temp = intList[k]
           intList[k] = intList[k-1]
           intList[k-1] = temp
           k = k - 1

intList = []

while True:
    num = input("Enter an integer or q to quit: ")

    if num.lower() == 'q':
        break
    num_int = int(num)
    intList.append(num_int)


print("Before insertion sort:",intList)
insertionSort(intList)
print("After insertion sort:",intList)