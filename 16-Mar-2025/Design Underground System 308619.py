# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.avarage = defaultdict(lambda : [0,0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None: 
        startStation, startTime = self.checkins[id]

        self.avarage[startStation+"-"+stationName][0] += t-startTime
        self.avarage[startStation+"-"+stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        duration, count = self.avarage[startStation+"-"+endStation]
        return duration/count

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)