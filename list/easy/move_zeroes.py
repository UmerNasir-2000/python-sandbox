# Brute

def move_zeroes_brute(nums):
    # store the non-zero elements in a list
    non_zero = []
    for i in range(len(nums)):
        if nums[i] != 0:
            non_zero.append(nums[i])

    # fill the rest of the list with zeroes
    for i in range(len(non_zero), len(nums)):
        non_zero.append(0)
        
# Better

def move_zeroes_better(nums):
    first_zero_index = -1
    length = len(nums)

    for i in range(length):
        if nums[i] == 0:
            first_zero_index = i
            break

    if first_zero_index == -1:
        return
        
    for i in range(first_zero_index + 1, length):
        if nums[i] != 0:
            nums[i], nums[first_zero_index] = nums[first_zero_index], nums[i]
            first_zero_index += 1

# Optimal

def move_zeroes(nums):
    last_non_zero_found_at = 0
    
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1