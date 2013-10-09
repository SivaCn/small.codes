
"""
    Convert the given infix expression to the postfix expression.
"""

class Converter():
    def __init__(self, exp):
        self.exp_lst = list(exp)
        self.stack = []
        self.output = []
        self.prec =    {
                            '(': 0, \
                            '+': 1, \
                            '-': 1, \
                            '*': 2, \
                            '/': 2
                        }

    def convert(self):
        print self.exp_lst
        for ele in self.exp_lst:
            if ele not in self.prec.keys() and ele != '(' and ele != ')':
                self.output.append(ele)
            elif ele == ')':
                stack_top = self.stack.pop()
                while stack_top != '(':
                    self.output.append(stack_top)
                    stack_top = self.stack.pop()

            else:
                self.stack.append(ele)

        print self.stack
        print self.output
        return ''.join(self.output)

expr = "((A+(B/E))*(C-D))"
obj = Converter(expr)
print obj.convert()

