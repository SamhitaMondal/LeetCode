class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        limit = left

        operations = sum(max(0, d - limit) for d in diff)
        remaining = k - operations

        diff = [min(d, limit) for d in diff]

        # Reduce the remaining differences by one
        # to use any leftover operations.
        for i in range(len(diff)):
            if remaining == 0:
                break
            if diff[i] == limit and diff[i] > 0:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)