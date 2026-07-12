class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        order = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in order:
                if stack and stack[-1] == order[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack         