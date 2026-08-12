class TimeMap:

    def __init__(self):
        self.mainMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mainMap:
            self.mainMap[key] = [[value,timestamp]]
        else:
            self.mainMap[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mainMap:
            return ""
        currList = self.mainMap[key]
        i = 0
        j = len(currList) - 1
        maxTimestamp = None
        while i <= j:
            mid = i + ((j - i) // 2)
            if currList[mid][1] < timestamp:
                if maxTimestamp == None or maxTimestamp < currList[mid][1]:
                    maxTimestamp = mid
                i = mid + 1
            elif currList[mid][1] > timestamp:
                j = mid - 1
            else:
                return currList[mid][0]
        if maxTimestamp == None:
            return ""
        return currList[maxTimestamp][0]
                
                
