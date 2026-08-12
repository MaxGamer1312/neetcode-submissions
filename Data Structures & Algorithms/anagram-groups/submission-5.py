class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for curr_str in strs:
            curr_dict = {}
            for char in curr_str:
                if char not in curr_dict:
                    curr_dict[char] = 0
                curr_dict[char] += 1
            curr_key = frozenset(curr_dict.items())
            if curr_key not in result_dict:
                result_dict[curr_key] = []
            result_dict[curr_key].append(curr_str)
        return list(result_dict.values())