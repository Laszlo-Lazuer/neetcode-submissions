class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            print(num)

            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i