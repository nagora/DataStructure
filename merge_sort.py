def divideData(arr):
    if len(arr)<2:
        return arr

    length =len(arr)

    mid = int(length/2)
    leftArray = arr[0:mid]
    rightArray = arr[mid:]
    divideData(leftArray)
    divideData(rightArray)
    return merge(arr,leftArray,rightArray)

def merge(arr,lefthalf,righthalf):
            print "MERGE -arr size "+str(len(arr))
            print "MERGE -lefthalf "+str(lefthalf)
            print "MERGE -righthalf "+str(righthalf)

            i = j = k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    arr[k]=lefthalf[i]
                    i=i+1
                else:
                    arr[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                arr[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                arr[k]=righthalf[j]
                j=j+1
                k=k+1
            print "AFTER MERGE "+str(arr)
            return arr


def mergeSort():

    data = [15,1,0,14,3,11]
    print divideData(data)
    print data


mergeSort()

