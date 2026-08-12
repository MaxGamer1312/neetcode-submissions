class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainList = []
        wordCollection = {}
        for i in strs:
            wordDict = {}
            for j in i:
                if j in wordDict:
                    wordDict[j] += 1
                else:
                    wordDict[j] = 1
            added = False
            for elementMainList in mainList:
                if wordDict == wordCollection[elementMainList[0]]:
                    elementMainList.append(i)
                    added = True
                    break
            if not added:
                mainList.append([i])
                wordCollection[i] = wordDict
        return(mainList)
        
        