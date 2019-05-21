import math
linearray=[10,20,25,12,15,40,30,55,37,22]
linearray.sort()
def BinarySearchalgorithm(array,low,size,x):
    if size >=1:
        mid = int(math.floor(low +(size-low)/2))
        if array[mid] ==x:
            return mid
        elif array[mid]>x and array[low]<=x:
            return BinarySearchalgorithm(array,low,mid-1,x)
        elif array[mid]<x and  array[size]>=x:
            return BinarySearchalgorithm(array,mid+1,size,x)
        else:
            return -1
    else:
        return -1

x=155
print("Linearsorted Array",linearray)
result =BinarySearchalgorithm(linearray,0,len(linearray)-1,x)
if result == -1:
    print("The element in the array is not found")
else:
    print("The array elemnet is found at index ",result)
