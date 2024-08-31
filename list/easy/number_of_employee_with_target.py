from typing import List


def number_of_employees_who_met_target(hours: List[int], target: int) -> int:
    count = 0
    for i in range(len(hours)):
        if hours[i] >= target:
            count += 1
    return count