class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainList = []
        wordCollection = {}
        for i in strs:
            wordDict = {}
            for j in i:
                if j in wordDict:
                    wordDict[j] = wordDict[j]+1
                else:
                    wordDict[j] = 1
            #print(wordDict)
            wordCollection[i] = wordDict
            if(len(mainList) == 0):
                test = []
                test.append(i)
                mainList.append(test)
            else:
                added = False
                for elementMainList in mainList:
                    if wordDict == wordCollection[elementMainList[0]]:
                        elementMainList.append(i)
                        added = True
                        break
                if(not added):
                    test = []
                    test.append(i)
                    mainList.append(test)
        
        return(mainList)
        
        