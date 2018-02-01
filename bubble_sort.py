def findMaxAndSwap(arr, indexRange, length):

    print length-(indexRange+1)
    for compareIndex in range(0, length-(indexRange+1) ):

        if( arr[compareIndex] > arr[compareIndex+1]):
            swap(arr, compareIndex+1 , compareIndex)

def swap(arr, index, maxIndex):
    arr[index],arr[maxIndex] = arr[maxIndex],arr[index]

def bubbleSort():

    data = [2, 9, 1, 8, 3 , 7, 12, 14, 11]
    length =len(data)

    for value in range(0, length-2 ):
         findMaxAndSwap(data, value , length)

    print data

bubbleSort()
