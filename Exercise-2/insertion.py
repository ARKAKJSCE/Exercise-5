def insertionSort(my_list):
    # for every element in our array
    for index in range(1, len(my_list)):
        current = my_list[index]
        position = index

        while position > 0 and my_list[position-1] > current:
            print("Swapped {} for {}".format(my_list[position], my_list[position-1]))
            my_list[position] = my_list[position-1]
            print(my_list)
            position -= 1

        my_list[position] = current

    return my_list

my_list = list()
n = int(input("Enter how many elements you want:"))
print ("Enter numbers in array: ")
for i in range(int(n)):
    n = int(input("num :"))
    my_list.append(int(n))
print ("ARRAY: "),my_list


print(insertionSort(my_list))