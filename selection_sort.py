def findMin(arr, minIndex, length):

    MIN = minIndex

    for compareIndex in range(minIndex+1,length):
        if(arr[compareIndex] < arr[MIN] ):
            MIN =  compareIndex
    return MIN

def swap(arr, index, minIndex):
    # t = arr[index]
    # arr[index] = arr[minIndex]
    # arr[minIndex] = t
    arr[index],arr[minIndex] = arr[minIndex],arr[index]

def selectionSort():

    data = [1, 1, 0, 3, 2 , 7]
    length =len(data)

    for value in range(0,len(data)):
        MIN_VALUE_INDEX = findMin(data, value , length)
        swap(data,value,MIN_VALUE_INDEX)

    print data

selectionSort()
