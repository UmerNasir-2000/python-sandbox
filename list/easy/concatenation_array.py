from typing import List


# Optimal

def get_concatenation(nums: List[int]) -> List[int]:
    length = len(nums)
    for i in range(length):
        nums.append(nums[i])
    return nums

# Could be done with Python Hacks Like : nums + nums : nums * 2: nums.extend(nums)

print(get_concatenation([1,2,1]))