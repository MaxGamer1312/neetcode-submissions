class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        i = 0
        j = len(self.data[key]) - 1
        while i <= j:
            middle_index = (i + j) // 2
            middle_element = self.data[key][middle_index]
            if middle_element[1] <= timestamp:
                i = middle_index + 1
            else:
                j = middle_index - 1
        self.data[key].insert(i, [value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        i = 0
        j = len(self.data[key]) - 1
        while i <= j:
            middle_index = (i + j) // 2
            middle_element = self.data[key][middle_index]
            if middle_element[1] == timestamp:
                return middle_element[0]
            if middle_element[1] < timestamp:
                i = middle_index + 1
            else:
                j = middle_index - 1
        if j < 0:
            return ""
        return self.data[key][j][0]
