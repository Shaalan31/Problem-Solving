class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while(len(stones) != 1):
            stones = sorted(stones,reverse=True)
            # print(stones)
            stones.append(stones[0]-stones[1])
            del stones[0]
            del stones[0]
        return stones[0]