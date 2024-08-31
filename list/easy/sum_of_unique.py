from typing import List


def sum_of_unique(nums: List[int]) -> int:
    map = {}
    sum = 0
    
    for i in range(len(nums)):
        map[nums[i]] = map.get(nums[i], 0) + 1
    
    for key, value in map.items():
        if value == 1:
            sum += key
            
    return sum

print(sum_of_unique(nums=[1,1]))