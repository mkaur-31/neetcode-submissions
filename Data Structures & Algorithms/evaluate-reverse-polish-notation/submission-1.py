import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+' : operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/":  lambda a, b: int(a / b)
        }

        for i in tokens:
            if i in ops:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                act = ops[i]
                res = act(val1,val2)
                stack.append(res)
            else:
                stack.append(i)
        return int(stack[0])