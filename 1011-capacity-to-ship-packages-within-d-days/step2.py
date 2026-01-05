class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)

        def is_shipable(cap: int) -> bool:
            needed_day = 1
            current_weight = 0

            for w in weights:
                if current_weight < cap:
                    current_weight += w
                else:
                    needed_day += 1
                    if needed_day > days:
                        return False
            return True
        
        while min_cap <= max_cap:
            mid = (min_cap + max_cap) // 2

            if is_shipable(mid):
                min_cap = mid + 1
            else:
                max_cap = mid - 1

        return min_cap