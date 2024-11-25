class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for char in expression:
            if char == ')':
                #  popping
                # evaluating expressions
                # pushing some result again
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop() 
            elif char != ',':
                stack.append(char)
