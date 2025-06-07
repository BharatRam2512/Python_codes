def findMedianSortedArrays(nums1,nums2):
    nums3=sorted(nums1+nums2)
    l=0
    h=len(nums3)
    num1=[1,3]
    if (len(nums3)%2)==1:
        mid=(((l+h)//2))
        x=float(nums3[mid])
        return x

    elif(len(nums3)%2==0):
        x=(l+h)//2
        y=x-1
        mid=((nums3[x]+nums3[y])/2)
        return mid
nums1=[1,3]
nums2=[2,4]
median=findMedianSortedArrays(nums1, nums2)
print(median)