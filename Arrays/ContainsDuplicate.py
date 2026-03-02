from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        repeat={}
        for i in range(len(nums)):
            dup=nums[i]
            if dup in repeat:
               return True
            else:
                repeat[nums[i]]=i
        return False
        