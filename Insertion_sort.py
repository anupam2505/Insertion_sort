#!/bin/python
def insertionSort(ar):    
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
n = m-1
a = ar[n]


def insertionSort(ar):
        for y in range(m-1,0,-1):
            if (a < ar[y-1] ):
                ar[y] = ar[y-1]
                arvalue = ' '.join(str(v) for v in ar)
                print arvalue
            elif (a >= ar[y-1]):
                ar[y]= a
                arvalue = ' '.join(str(v) for v in ar)
                print arvalue
       
insertionSort(ar)