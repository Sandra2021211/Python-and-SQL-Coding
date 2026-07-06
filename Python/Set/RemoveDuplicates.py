#This is different from Remove Duplicates from Sorted Array because the input here isn’t necessarily sorted.

# Input:
# nums=[3,2,2,1,3]

# Output:
# [3,2,1]

# Code:

def removeDuplicates(nums):
    seen=set()
    answer=[]

    for num in nums:
        if num not in seen:
            seen.add(num)
            answer.append(num)

    return answer
