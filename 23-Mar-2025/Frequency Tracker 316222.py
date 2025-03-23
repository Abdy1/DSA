# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.num_count = defaultdict(int)
        self.freq_count = defaultdict(int)
    
    def add(self, number: int) -> None:
        current_freq = self.num_count[number]

        if current_freq > 0:
            self.freq_count[current_freq] -= 1

        self.num_count[number] += 1
        new_freq = current_freq + 1
        self.freq_count[new_freq] += 1



        
    def deleteOne(self, number: int) -> None:
        curr_frequency = self.num_count[number]

        if curr_frequency == 0:
            return 

        self.freq_count[curr_frequency] -= 1
        self.num_count[number] -= 1

        new_freq = curr_frequency - 1

        if new_freq > 0:
            self.freq_count[new_freq] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0
            
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)