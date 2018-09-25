from ArrayStack import ArrayStack


def eval_expr(expression):
    operand_stack = ArrayStack()
    operator_stack = ArrayStack()

    for i in range(len(expression)):
        if expression[i] == '(':
            continue
        elif expression[i] in '0123456789':
            operand_stack.push(int(expression[i]))
        elif expression[i] in '+-*/':
            operator_stack.push(expression[i])
        elif expression[i] == ')':
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            op = operator_stack.pop()
            operand_stack.push(compute(op1,op2,op))

    return operand_stack.pop()

def compute(op1, op2, op):
    if op == '+':
        return op1+op2
    elif op == '-':
        return op1-op2
    elif op == '*':
        return op1*op2
    elif op == '/':
        return op1/op2

if __name__ == '__main__':

    print eval_expr('(1+(4*5))')
    print eval_expr('(1+((2+3)*(4*5)))')
    print eval_expr('12')
    print eval_expr('()')

    
