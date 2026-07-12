class Solution:
    def isValid(self, s: str) -> bool:
        order = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in order:
                if len(stack) == 0 or stack[-1] != order[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack
