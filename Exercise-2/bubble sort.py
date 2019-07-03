# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	# Traverse through all array elements
	for i in range(len(arr)):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

arr = list()
n = int(input("Enter how many elements you want:"))
print ("Enter numbers in array: ")
for i in range(int(n)):
    n = int(input("num :"))
    arr.append(int(n))
print ("ARRAY: "),arr


bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i]), 
