
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            return sum(int(d) for d in str(x))

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {value: i for i, value in enumerate(nums)}
        ans = 0

        for i in range(len(nums)):
            if nums[i] != arr[i]:
                ans += 1

                j = pos[arr[i]]

                pos[nums[i]] = j
                pos[arr[i]] = i

                nums[i], nums[j] = nums[j], nums[i]

        return ans
