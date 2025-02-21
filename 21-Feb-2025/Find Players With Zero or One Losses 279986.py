# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []
        winners = { item[0] for item in matches}
        losers = [item[1] for item in matches]

        never_lost = list(winners - set(losers))
        never_lost.sort()
        answer.append(never_lost)

        losers_counter = {}
        for i in range(len(losers)):
            losers_counter[losers[i]] = losers_counter.get(losers[i],0)+1

        lost_once = [item for item, freq in losers_counter.items() if freq == 1]
        lost_once.sort()


        return [never_lost, lost_once]


        
        
        