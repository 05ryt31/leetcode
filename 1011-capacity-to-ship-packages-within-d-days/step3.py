class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)

        def is_shipable(cap: int) -> bool:
            current_weight = 0
            needed_days = 1

            for w in weights:
                if current_weight + w <= cap:
                    current_weight += w
                else:
                    needed_days += 1
                    current_weight = w
                    
                    if needed_days > days:
                        return False
            return True

        while min_cap < max_cap:
            mid = (min_cap + max_cap) // 2
            
            if is_shipable(mid):
                max_cap = mid
            else:
                min_cap = mid + 1

        return min_cap