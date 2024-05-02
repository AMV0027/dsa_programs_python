n = int(input("Enter the size of the array : "))

arr = []

for i in range(n):
    num = int(input(f"element [{i+1}] : "))
    arr.append(num)
print(arr)

key = int(input("Enter the element to be searched : "))

low = 0
high = n-1
mid = int((low + high) /2)

while(low <= high):
    if(key > arr[mid]):
        low = mid+1
    elif(key == arr[mid]):
        print(f"Element found at index {mid} !")
        break
    else:
        high = mid -1

    mid = int((low+high)/2)


