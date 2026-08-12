class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        leftDict = {s[0]:0}
        currList = [s[0]]
        maxLength = 1
        Ileft = 0
        for Iright in range(1, len(s)):

            if s[Iright] in leftDict:
                if maxLength < len(leftDict):
                    maxLength = len(leftDict)
                foundDupe = False
                while not foundDupe:
                    currElement = currList.pop(0)
                    leftDict.pop(currElement)
                    if currElement == s[Iright]:
                        foundDupe = True
                leftDict[s[Iright]] = Iright
                currList.append(s[Iright])                
                Ileft = leftDict[currList[0]]

            else:
                leftDict[s[Iright]] = Iright
                currList.append(s[Iright])
        return max(maxLength, len(leftDict))