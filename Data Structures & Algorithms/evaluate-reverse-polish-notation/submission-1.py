class Solution:
    


    def evalRPN(self, tokens: List[str]) -> int:

        def operate(a, b, symbol):
            if symbol == '+':
                return a + b
            elif symbol == '-':
                return a - b
            elif symbol == '*':
                return a * b
            elif symbol == '/':
                return int(a / b) 

        stack = []
        symbol = ["+", "-", "*", "/"]



        for token in tokens:
            if token in symbol:
                b = stack.pop()
                a = stack.pop()
                result = operate(a, b, token)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]