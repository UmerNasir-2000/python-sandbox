from typing import List

# Optimal 

def running_sum(nums: List[int]) -> List[int]:
    for i in range(len(nums)-1):
        nums[i+1] = nums[i] + nums[i+1]
    
    return nums

print(running_sum([1,2,3,4]))