class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen=set()
        duplicates=[]

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                duplicates.append(num)
        return duplicates