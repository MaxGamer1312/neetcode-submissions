class Solution:
    def isValid(self, s: str) -> bool:
        mapParen = {
            '(':')',
            '{':'}',
            '[':']'
        }
        test = []
        for i in s:
            print(i)
            if i in mapParen:
                test.append(i)
            else:
                if len(test) == 0:
                    return False
                if i != mapParen[test[-1]]:
                    return False
                else:
                    test.pop()
            
        if len(test) == 0:
            return True
        return False
