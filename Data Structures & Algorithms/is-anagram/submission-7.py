class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test = {}
        for i in s:
            if i in test:
                test[i] = test[i] + 1
            else:
                test[i] = 1
        for i in t:
            if i in test:
                test[i] = test[i] - 1
                if(test[i] == -1):
                    return False
                elif(test[i] == 0):
                    del test[i]
            else:
                return False
        if(len(test) == 0):
            return True
        return False
