# first approach
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        check = set()
        for num in nums:
            check.add(num)

        if len(nums) == len(check):
            return False
        return True


# more simple approach -> O(n) time complexity/ O(n) space complexity
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


# second approach
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        check = {}
        for index, num in enumerate(nums):
            if num in check:
                return True
            check[num] = index
        return False


# more simple approach using set--> O(n) time complexity/ O(n) space complexity
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# less efficient approach / Bruce Force, O(n^2) time complexity>
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# less efficient approach -> O(nlogn) time complexity/ O(1) space complexity
class Solution:
    def hasDupicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, lent(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
