class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        compare_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for char in s:
            if char in compare_dict:
                stack.append(char)
                continue
            if not stack or compare_dict[stack[-1]] != char:
                return False
            stack.pop()
        return not stack