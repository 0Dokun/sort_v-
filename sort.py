# PALINDROME
word = "LEVEL"
word= word.lower()
if word ==word[::-1]:
    print ("True")
else:
    print ("False")

word = "madaf"
word= word.lower()
if word ==word[::-1]:
    print ("True")
else:
    print ("False")

#BUBBLE SORT
def bubble_sort (lis):
    size = len(lis)

    for i in range (size):
        for j in range (size-i-1):
            if lis[j] < lis [j+1]:
                lis[j], lis[j+1] = lis[j+1],lis[j]
    return lis

list = [64,34,25,12,22,11,90]
print(bubble_sort(list))

#insertion sort
def insertion_sort(lis):
    num = len(lis)
    for i in range(1,num):
        key = lis[i]
        j = i-1
        while j >=0 and key < lis[j]:
            lis [j + 1] = lis [j]
            j -= 1 
        lis [j + 1] = key
    return lis
list = [4,9,2,7,5,8,3]
print (insertion_sort(list))

#insertion sort
def insertion_sort_words(lett):
    num = len(lett)
    for i in range(1,len(lett)):
        key = lett[i]
        j = i-1
        while j >= 0 and lett[j]>key:
            lett[j+1] = lett[j]
            j -= 1
        lett[j + 1] = key
    return lett

words = ["banana", "Apple", "cherry", "date"]
print(insertion_sort_words(words)) 

#insertion sort
def insertion_sort(num):
    n = len(num)
    for i in range(1,n):
        key = num[i]
        j = i-1
        while j >= 0 and key < num[j]:
            num [j + 1] = num[j]
            j -=1
        num [j +1] = key
    return num 
numb = [-1,5,3,4,0]
print(insertion_sort(numb))

#BUBBLE SORT
def bubble_sort (lis):
    size = len(lis)

    for i in range (size):
        for j in range (size-i-1):
            if lis[j] < lis [j+1]:
                lis[j], lis[j+1] = lis[j+1],lis[j]
    return lis

list = [64,34,25,12,22,11,90]
print(bubble_sort(list))

#selection sort
list = [64, 25, 12, 22, 11]
def selection_sort(dog):
    n = len(dog)
    for i in range (n):
        min_idx = i
        for j in range (i +1, n):
            if dog[min_idx] > dog[j]:
             min_idx = j
        dog[i], dog[min_idx] = dog[min_idx], dog[i]

    return dog
print (selection_sort(list))

#selection sort
data = [('a', 3), ('b', 1), ('c', 2)]
def sort_tuples(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range (i +1, n):
            if arr[min_idx][1] > arr[j][1]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx] , arr[i]
    return arr

print(sort_tuples(data))
# Should print: [('b', 1), ('c', 2), ('a', 3)]

#merge sort
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) 
        L = arr[:data]  
        R = arr[data:]  

        merge_sort(L)  
        merge_sort(R)  

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1
    return data

# Example usage:
my_list = [12, 11, 13, 5, 6, 7]
sorted_list = merge_sort(my_list)
print("Sorted list is:", sorted_list)
# Output: Sorted list is: [5, 6, 7, 11, 12, 13]
#q_sort
import random

def q_sort(arr):
    if len(arr)<= 1:
        return arr
    pivot = random.choice(arr)

    left = [ x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return q_sort(left) + middle +q_sort(right)

arr = [7,2,1,6,8,5,3,4]
print(q_sort(arr))


def quick_sort(data):
    _quick_sort_recursive(data, 0, len(data) - 1)
    return data


def _quick_sort_recursive(data, low, high):
    if low < high:   
        pi = _partition(data, low, high)
        _quick_sort_recursive(data, low, pi - 1)
        _quick_sort_recursive(data, pi + 1, high)
def _partition(data, low, high):
    i = (low - 1)         
    pivot = data[high]     
    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return (i + 1)


# Example usage:
my_list = [10, 7, 8, 9, 1, 5]
sorted_list = quick_sort(my_list)
print("Sorted list is:", sorted_list)
# Output: Sorted list is: [1, 5, 7, 8, 9, 10]

