class Solution:

    def encode(self, strs: List[str]) -> str:
        mainString = ""
        for i in strs:
            mainString += str(len(i))+ "#" + i
        print(mainString)
        return mainString
    def decode(self, s: str) -> List[str]:
        temp = []
        i = 0
        while i in range(len(s)): 
            print(i)
            j = i
            wordString = ""
            while True:
                if(s[j] == "#"):
                    break;
                wordString += s[j]
                j+=1
            wordCount = int(wordString)
            i+=len(wordString)+1
            tempString = s[i:i+wordCount]
            temp.append(tempString)
            i+=wordCount
        return temp
