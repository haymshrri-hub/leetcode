
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        k -= 1  # Convert to 0-based indexing

        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        result = []

        for i in range(n - 1, -1, -1):
            index = k // fact[i]
            result.append(str(nums.pop(index)))
            k %= fact[i]

        return ''.join(result)
