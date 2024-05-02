def partition(arr, low, high):
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

if __name__ == '__main__':
    arr = []
    n = int(input("Enter number of items : "))

    for i in range(n):
        num = int(input(f"Element {i+1} : "))
        arr.append(num)

    print("\n Given array : ")
    print(arr)

    quicksort(arr, 0, n-1)

    print("\nSorted array : ")
    print(arr)