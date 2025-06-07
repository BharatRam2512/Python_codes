def binary_search(arr,n,key):
    l=0
    h=n
    def rbs(l,h,key):
        if l==h:
            if arr[l]==key:
                return l
            return "key element not found"
        elif l<=h:
            mid=(l+h)//2
            if arr[mid]==key:
                return mid
            elif key>=arr[mid]:
                return rbs(mid+1,h,key)
            else:
                return rbs(l,mid-1,key)
        else:
            return "key element not found"
    return rbs(l,h,key)

arr1=list(map(int,input("Enter the elements of the array: ").split()))
arr=sorted(set(arr1))
print("Sorted array:", arr)
n=len(arr)
key=int(input("Enter the key to be searched: "))
print("Key found at index:", binary_search(arr,n,key))