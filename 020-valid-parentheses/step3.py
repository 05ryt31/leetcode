## 別解
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {"()": ")", "[]": "]", "{": "}"}

        for c in s:
            if c in open_to_close:
                if stack and stack[-1] == open_to_close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False