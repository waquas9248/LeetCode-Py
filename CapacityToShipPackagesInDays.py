# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        ## max weight overall possible that can be shipped will be in range [max(weights), sum(weights)]
        min_weight = max(weights)
        max_weight = sum(weights)

        mid = (min_weight + max_weight)/2

        low = min_weight
        high = max_weight
        ans = -1

        ## to find and converge at the best fit, binary search over the range
        while low <= high:

            mid = (int) ( (low+high)/2 )
                
            valid = self.check(mid, weights, days)

            if( valid == False ):
                low = mid + 1
            else:
                high = mid - 1
                ans = mid
            
        return ans  

    def check(self, mid: int, weights: List[int], days: int) -> bool:
        sum_weights = 0
        curr_days = 0
        
        for weight in weights:

            sum_weights = sum_weights + weight

            if( sum_weights > mid ):
                curr_days = curr_days + 1
                sum_weights = weight
            elif (sum_weights == mid):
                curr_days = curr_days + 1
                sum_weights = 0
            else:
                pass

        if( sum_weights != 0 ):
            curr_days = curr_days + 1

        return curr_days <= days  
