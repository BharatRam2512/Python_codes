def binary_search(arr,n,key):
    low=0
    high=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return 0
arr1=list(map(int,input("Enter the elements of the array: ").split()))
arr=sorted(set(arr1))
print("Elements after sorting: ",arr)
n=len(arr)
key=int(input("Enter the element to be searched: "))
<<<<<<< HEAD
print("The result present in the index: ",binary_search(arr,n,key))
=======
print("The result present in the index: ",binary_search(arr,n,key))
>>>>>>> 1011a9321961b35d79e7764f639be989f0550832
