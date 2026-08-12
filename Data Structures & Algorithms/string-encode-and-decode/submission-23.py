class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for curr_str in strs:
            result.append(f"{len(curr_str)}/{curr_str}")
        print(result)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        start_of_count = 0
        i = 0
        while i < len(s):
            if s[i] != '/':
                i += 1
                continue
            curr_len = int(s[start_of_count:i])
            result.append(s[i + 1:(i + 1) + curr_len])
            i += curr_len + 1
            start_of_count = i
        return result

