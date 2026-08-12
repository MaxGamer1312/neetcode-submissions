class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = {}
        for i in range(len(s)):
            current_char_s = s[i]
            current_char_t = t[i]
            if current_char_s not in char_dict:
                char_dict[current_char_s] = 0
            if current_char_t not in char_dict:
                char_dict[current_char_t] = 0  
            char_dict[current_char_s] += 1
            char_dict[current_char_t] -= 1
        for value in char_dict.values():
            if value != 0:
                return False
        return True