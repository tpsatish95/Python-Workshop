from collections import defaultdict
import operator

freqMap = defaultdict(int)

with open("content.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        for word in line.split():
            freqMap[word.strip()] += 1

sortedFreq = sorted(freqMap.items(),key = operator.itemgetter(1), reverse=True)[:10]
print(sortedFreq)
