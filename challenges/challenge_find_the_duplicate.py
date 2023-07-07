def find_duplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if not isinstance(nums[i], int) or nums[i] <= 0:
            print(nums[i])
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False


find_duplicate([1, 2, 2, 3, 4])
