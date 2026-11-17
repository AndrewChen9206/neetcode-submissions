class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = [0] * 2

        for bill in bills:
            if bill == 5:
                wallet[0] += 1
            elif bill == 10:
                if wallet[0] > 0:
                    wallet[0] -= 1
                    wallet[1] += 1
                else:
                    return False
            else:
                if wallet[0] > 0 and wallet[1] > 0:
                    wallet[0] -= 1
                    wallet[1] -= 1
                elif wallet[0] >= 3:
                    wallet[0] -= 3
                else:
                    return False
        
        return True