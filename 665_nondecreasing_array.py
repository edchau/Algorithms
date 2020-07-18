class Solution:
	"""
	665. Non-decreasing Array
	Input: nums = [4,2,3]
	Output: true
	Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
	"""
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if modified is not None:
                    return False
                modified = i
        return (modified is None or modified == 0 or modified == len(nums) - 2 or nums[modified-1] <= nums[modified+1] or nums[modified] <= nums[modified+2])