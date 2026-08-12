class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        frequencyMap[1] = []
        currPlace = {}
        keyList = []
        keyList.append(1);
        answer = []
        for i in nums:
            if i not in currPlace:
                frequencyMap[1].append(i)
                currPlace[i] = 1
            else:
                frequencyMap[currPlace[i]].remove(i)
                if currPlace[i]+1 not in frequencyMap:
                    frequencyMap[currPlace[i]+1] = []
                    keyList.append(currPlace[i]+1);
                frequencyMap[currPlace[i]+1].append(i)
                currPlace[i] += 1
                
        answer = []
        keyList.sort(reverse=True)
        count = 0
        for i in keyList:
            for j in frequencyMap[i]:
                if(count == k):
                    break
                answer.append(j)
                count+=1
        print(answer)
        return answer
