from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        # Store all numbers with their indices
        for i, n in enumerate(nums):
            indices[n] = i

        # Find the pair
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return [] 
