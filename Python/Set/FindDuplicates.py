# Input:
# nums=[1,2,2,3,4,4]

# Output:
# [2,4]

# Code:
def findDuplicates(nums):
    seen=set()

    duplicates=[]

    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates