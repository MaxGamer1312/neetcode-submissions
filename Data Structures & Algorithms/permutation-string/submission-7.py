class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        for char in s1:
            count1[ord(char) - ord('a')] += 1
        count2 = [0] * 26
        for i in range(len(s2)):
            if count1 == count2:
                return True
            count2[ord(s2[i]) - ord('a')] += 1
            if i < len(s1):
                continue
            count2[ord(s2[i-len(s1)]) - ord('a')] -= 1
        if count1 == count2:
            return True
        return False