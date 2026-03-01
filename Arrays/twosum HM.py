from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ihaveseen={}
        for i in range(len(nums)):
            want=target-nums[i]
            if want in ihaveseen:
                return ihaveseen[want],i
            ihaveseen[nums[i]]=i
