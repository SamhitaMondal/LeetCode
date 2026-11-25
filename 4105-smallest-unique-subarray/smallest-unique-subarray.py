class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:

        n = len(nums)

        BASE = 911382323
        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9

        def check(length):

            freq = {}

            hash1 = 0
            hash2 = 0

            power1 = pow(BASE, length, MOD1)
            power2 = pow(BASE, length, MOD2)

            # Calculate hash of first window
            for i in range(length):
                hash1 = (hash1 * BASE + nums[i]) % MOD1
                hash2 = (hash2 * BASE + nums[i]) % MOD2

            freq[(hash1, hash2)] = 1

            # Slide the window
            for i in range(length, n):

                old = nums[i - length]
                new = nums[i]

                hash1 = (hash1 * BASE + new - old * power1) % MOD1
                hash2 = (hash2 * BASE + new - old * power2) % MOD2

                key = (hash1, hash2)

                freq[key] = freq.get(key, 0) + 1

            # Check if any subarray appears exactly once
            return any(count == 1 for count in freq.values())

        # Binary Search
        left = 1
        right = n

        while left < right:

            mid = (left + right) // 2

            if check(mid):
                right = mid

            else:
                left = mid + 1

        return left