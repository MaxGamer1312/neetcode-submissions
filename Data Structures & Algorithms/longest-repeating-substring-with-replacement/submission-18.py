class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        width = 0
        i = 0
        max_char = 'A'
        for j in range(len(s)):
            width = j-i+1
            counts[ord(s[j])-ord('A')] += 1
            if counts[ord(s[j])-ord('A')] > counts[ord(max_char)-ord('A')]:
                max_char = s[j]
            if width - counts[ord(max_char)-ord('A')] > k:
                counts[ord(s[i])-ord('A')] -= 1
                for l in range(len(counts)):
                    if counts[l] > counts[ord(max_char)-ord('A')]:
                        max_char = chr(l+ord('A'))
                i += 1
        width = j-i+1
        return width