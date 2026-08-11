#Bubble sort
def Bubble_sort(data):
    n = len(data)

    for i in range (n):
        for j in range (0,n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        print (data)

#selection sort
def selection_sort(data):
    n = len(data)
    for i in range (n):
        min_idx = i
        for j in range (i +1, n):
            if data[min_idx] > data[j]:
             min_idx = j
        if min_idx !=i:
           data[i], data[min_idx] = data [min_idx], data[i]
           print(data)

#Insertion sort
def insertion_sort(data):
    n = len(data)
    for i in range(1,n):
        key = data[i]
        j = i-1
        while j >=0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1 
        data [j + 1] = key
        print(data)

#Quick sort
def quick_sort(data):
  _quick_sort_recursive(data,0,len(data)- 1)
  return data
def _quick_sort_recursive(data, low, high):
    if low < high:   
      pi = _partition(data, low, high)
      print(data)
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
    return i + 1

#merge sort 
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        L = data[:mid]  
        R = data[mid:]  
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
        print("steps:", data)
    return data

while True:
  
# Data types
  print ("=========================")
  print ("   SORTING VISUALISER    ")
  print ("=========================")
  print ("Choose your data type")
  print ("1. Numbers ")
  print ("2. Characters")
  print ("3. words")

  data_choice = input("Enter choice: ")

  if data_choice == "1":
     data = input("Enter number seprated by space: ")
     data = list(map(int,data.split()))

  elif data_choice == "2":
     data = input("Enter characters seprated by space: ")
     data = data.split()

  elif data_choice == "3":
     data = input("Enter words seprated by space: ")
     data = data.split()

  else:
     print("invalid choice.")
     continue

#menu
  print ("=========================")
  print ("   SORTING VISUALISER    ")
  print ("=========================")

  print ("1. Bubble sort")
  print ("2. Selection sort")
  print ("3. Insertion sort")
  print ("4. Quick sort")
  print ("5. Merge sort")
  print ("6. EXIT")

  choice = input("Enter your choice: ")

#Bubble sort
  
  if choice == "1":


    print("\nOriginal list:")
    print(data)

    print("\nSorting...")

    Bubble_sort(data)
    print("\nSorted list:")
    print(data)
    input("\nPress Enter to retuen to menu...")

#selection sort
  
  elif choice == "2":
  
    print("\nOriginal list:")
    print(data)
    print("\nSorting...")

    selection_sort(data)
    print("\nSorted list:")
    print(data)
    input("\nPress Enter to retuen to menu...")

#insertion sort

  elif choice == "3":
  
    print("\nOriginal list:")
    print(data)        
    print("\nSorting...")
    
    insertion_sort(data)
    print("\nSorted list:")     
    print(data)
    input("\nPress Enter to retuen to menu...")

#quick sort
  elif choice == "4":
    
    print("\nOriginal list:")
    print(data)        
    print("\nSorting...")
      
    data = quick_sort(data)
    print("\nSorted list:")     
    print(data)
    input("\nPress Enter to retuen to menu...")

#merge sort 
  elif choice == "5":
    
    print("\nOriginal list:")
    print(data)        
    print("\nSorting...")
      
    data = merge_sort(data)
    print("\nSorted list:")     
    print(data)
    input("\nPress Enter to retuen to menu...")

#EXIT
  elif choice =="6":
  
    print("Goodbye!")
    break 
  else:
    print("Invalid choice.")
