class FreqStack:

    def __init__(self):
        self.stack = []
        self.highestFreq = 0 #reduce this
        self.freqMap = {} # per num
        self.freqSet = collections.defaultdict(list) # freq of groups

    def push(self, val: int) -> None:
        # self.stack.append(val) # Not needed with frequency-grouping strategy
        self.freqMap[val] = self.freqMap.get(val,0) + 1
        f = self.freqMap[val]
        if f > self.highestFreq:
            self.highestFreq = f
        self.freqSet[f].append(val)

    def pop(self) -> int:
        val = self.freqSet[self.highestFreq].pop()
        self.freqMap[val] -= 1 
        if not self.freqSet[self.highestFreq]:
            self.highestFreq -= 1
        return val