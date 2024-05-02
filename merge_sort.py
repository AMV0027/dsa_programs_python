def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m

    l = [0]*n1
    r = [0]*n2
    for i in range(0, n1):
        l[i] = arr[l+i]
    for j in range(0, n2):
        r[j] = arr[m+1+j]
        i=0
        j-0
        k=1
    while (i<n1 and j<n2):
        if(l[i] <= r[j]):
            arr[k]=l[i]
            i+=1
        else:
            arr[k]=r[j]
            j+=1
        k+=1

    while i<n1:
        arr[k] = l[i]
        i+=1
        k+=1
    while j<n2:
        arr[k] = r[j]
        j+=1
        k+=1




def mergesort(arr, l, r):
    if l<r:
        m = int(l+(r-1)/2)
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)

        merge(arr, l, m, r)



n = int(input("Enter array size : "))

arr = []
for i in range(n):
    num = input(f"element {i} : ")
    arr.append(num)

print("Before sorted : ")
print(arr)

mergesort(arr, 0, n-1)

print("After sorted : ")
print(arr)