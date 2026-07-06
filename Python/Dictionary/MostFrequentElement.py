# Input:

# nums = [1,2,2,3,3,3]

# Output: 3

# Code:

def mostFrequent(nums):

    frequency={}

    for num in nums:
        frequency[num]=frequency.get(num,0)+1

    answer=None
    maximum=0

    for num, count in frequency.items():
        if count>maximum:
            maximum=count
            answer=num
    return answer
