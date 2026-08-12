class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for curr_str in strs:
            curr_id = 26 * [0]
            for char in curr_str:
                curr_id[ord(char) - ord('a')] += 1
            curr_key = tuple(curr_id)
            if curr_key not in result_dict:
                result_dict[curr_key] = []
            result_dict[curr_key].append(curr_str)
        return list(result_dict.values())
