# Time O(n)
# Space O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for i in range(n):
            diff = n - i
            if diff == citations[i] or diff < citations[i]:
                return diff
        return 0

# Time O(log n)
# Space : O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low = 0
        high = n-1
        while low <= high:
            mid = low + (high - low) // 2
            diff = n - mid
            if diff == citations[mid]:
                return diff
            elif diff > citations[mid]:
                low = mid + 1
            else: high = mid - 1
        return n - low
        