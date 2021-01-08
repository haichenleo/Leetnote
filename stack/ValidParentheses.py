# https://leetcode-cn.com/problems/implement-stack-using-queues/

# invalid的三种情形：
# 1. {
# 2. }{
# 3. {]

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = list()
        left = {"(", "[", "{"}
        parentheses_pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for i in s:
            if i in parentheses_pairs:
                # 情形 2+3
                if not stack or stack[-1] != parentheses_pairs[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        # 情形 1
        return not stack


class Solution2:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = list()
        for c in s:
            if c == '{':
                stack.append('}')
            elif c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif len(stack) == 0 or c != stack.pop():
                return False
        return not stack


result = Solution2().isValid("()")
print(result)