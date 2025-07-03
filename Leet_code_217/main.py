def containsDuplicate(nums) :
    x=set()
    for i in nums:
        if i in x:
            return True
        x.add(i)
    return False

nums=[1,2,3,1]
print(containsDuplicate(nums))