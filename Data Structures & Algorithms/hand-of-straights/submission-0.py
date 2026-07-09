class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        card_remain_dict = {}
        hand.sort()
        
        for card in hand:
            if card not in card_remain_dict:
                card_remain_dict[card] = 1
            else:
                card_remain_dict[card] += 1
        
        for card in hand:
            if card_remain_dict[card] == 0:
                continue
            
            while card_remain_dict[card] != 0:
                card_remain_dict[card] -= 1

                for i in range(1, groupSize):
                    if card + i not in card_remain_dict or card_remain_dict[card + i] == 0:
                        return False

                    card_remain_dict[card + i] -= 1
        
        return True