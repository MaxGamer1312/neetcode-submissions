class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        need = 0
        for elem_t in t:
            if elem_t in count_t:
                count_t[elem_t] += 1
            else:
                need += 1
                count_t[elem_t] = 1
        i = 0
        j = 0
        result_index = [-1, -1]
        current_count = {}
        have = 0
        while j < len(s):
            if s[j] in count_t:
                if s[j] in current_count:
                    current_count[s[j]] += 1
                else:
                    current_count[s[j]] = 1
                if count_t[s[j]]-current_count[s[j]] == 0:
                    have += 1

            while i <= j and have >= need:
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
