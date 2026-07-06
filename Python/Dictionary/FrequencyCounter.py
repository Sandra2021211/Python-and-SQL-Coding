# Pattern : Dictionary (Hash Map)

# ⸻

# Problem

# Given
# nums = [1,2,2,3,3,3]

# Returns:
# {
# 1:1,
# 2:2,
# 3:3
# }

# Code:

def frequency_counter(nums):
    frequency = {}
    
    for num in nums:
        frequency[num] = frequency.get(num,0)+1
    
    return frequency

