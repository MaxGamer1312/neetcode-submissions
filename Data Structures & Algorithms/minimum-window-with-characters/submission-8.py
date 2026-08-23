class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for elem_t in t:
            if elem_t in count_t:
                count_t[elem_t] += 1
            else:
                count_t[elem_t] = 1
        i = 0
        j = 0
        result_index = [-1, -1]
        current_count = {}
        while j < len(s):
            if s[j] in count_t:
                if s[j] in current_count:
                    current_count[s[j]] += 1
                else:
                    current_count[s[j]] = 1
            if self.is_valid(current_count, count_t):
                while i <= j:
                    if result_index == [-1, -1] or j-i < result_index[1]-result_index[0]:
                        result_index[0] = i
                        result_index[1] = j
                    if s[i] in current_count:
                        if current_count[s[i]]-1 < count_t[s[i]]:
                            break
                        current_count[s[i]] -= 1
                    i += 1
            j += 1
        if result_index == [-1, -1]:
            return ""
        return s[result_index[0]:result_index[1]+1]

    def is_valid(self, s_dict, t_dict):
        for key in t_dict:
            if key not in s_dict or t_dict[key] > s_dict[key]:
                return False
        return True
