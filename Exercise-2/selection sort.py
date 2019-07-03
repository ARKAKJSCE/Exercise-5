def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = list()
n = int(input("Enter how many elements you want:"))
print ("Enter numbers in array: ")
for i in range(int(n)):
    n = int(input("num :"))
    alist.append(int(n))
print ("ARRAY: "),alist

selectionSort(alist)
print(alist)
