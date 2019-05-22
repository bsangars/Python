# Bubble Sort for an Array.
def BubbleSort(Array):
    def swap(i,j):
        Array[i],Array[j] = Array[j],Array[i]
    n=len(Array)
    swapped =True
    x= -1
    while swapped:
        swapped=False
        x=x+1
        for i in range(1,n-x):
            if Array[i-1]>Array[i]:
                swap(i-1,i)
                swapped=True
    return Array

SampleArray =[2,1,2.5,1.1,6,4,7,5.5,7.1,10, 8,9,9.9]
TextArray =['1Alpha','AArin','Ja1ck','Charlie','Bingo','Jil9l','Zebra','Debra','Dustin']
BubblesortedArray =BubbleSort(TextArray)
print(BubblesortedArray)
