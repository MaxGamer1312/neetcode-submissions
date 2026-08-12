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
            if current_char_s in char_dict and char_dict[current_char_s] == 0:
                char_dict.pop(current_char_s)
            if current_char_t in char_dict and char_dict[current_char_t] == 0:
                char_dict.pop(current_char_t)
        if char_dict:
            return False
        return True