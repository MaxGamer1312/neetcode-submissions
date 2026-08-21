class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        i = 0

        for j in range(len(s)):
            if j == len(s)-1 or s[j] != s[j+1]:
                temp_result = j-i+1
                temp_k = k
                for l in range(j+1, len(s)+1):
                    if l >= len(s) or s[j] != s[l]:
                        if l >= len(s) or temp_k <= 0:
                            temp_result += l-(j+1)+min(temp_k, i-0)
                            break
                        else:
                            temp_k -= 1
                if result < temp_result:
                    result = temp_result
                i = j+1
        return result