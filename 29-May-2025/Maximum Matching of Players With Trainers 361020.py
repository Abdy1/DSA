# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
    
        m, n = 0, 0
        matching = 0
        while m < len(players) and n < len(trainers):
            if players[m] <=  trainers[n]:
                m, n = m+1, n+1
                matching += 1
            else:
                n  += 1
        return matching
        