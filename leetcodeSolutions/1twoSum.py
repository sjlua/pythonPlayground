class Solution:
    """
    O(N^2)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                

class OptimisedSolution:
    """
    O(N)

    Use a hashmap (dictionary), as operations on a dict are O(1). Use the in operator.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_values = {}

        for i in range(len(nums)):
            complement = target - nums[i]