def binary_search(arr,item):
    first = 0
    last = len(arr)-1

    while first <= last:
        mid = (first+last)//2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            last = mid - 1
        else:
            first = mid + 1
    return None

def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    newarr = []

    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

def window_resize(window,width,height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2)-(width/2))
    y = int((screen_height/2)-(height/2))

    window.geometry(f"{width}x{height}+{x}+{y}")

def linear_search(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

def recursive_binary_search(list,target):
    
    if len(list) == 0:
        return False
    else:
        mid = (len(list) - 1)//2
        guess = list[mid]

        if guess == target:
            return guess
        elif guess > target:
            return recursive_binary_search(list[:mid],target)
        else:
            return recursive_binary_search(list[mid+1:],target)


    

            



