def isMatching(openingBracket, closingBracket):
    if (openingBracket == '{' and closingBracket == '}'):
        return True
    if (openingBracket == '(' and closingBracket == ')'):
        return True
    if (openingBracket == '[' and closingBracket == ']'):
        return True
    return False
def isBalanced(expression):
    stack = []
    for i in range(len(expression)):
        if (expression[i] == '{' or expression[i] == '(' or expression[i] == '['):
            stack.append(expression[i])
        else:
            if (len(stack) == 0):
                return False
            if (isMatching(stack.pop(), expression[i]) is not True):
                return False
    if (len(stack) == 0):
        return True
    return False
if __name__ == '__main__':
    expression1 = "[[()]]"
    expression2 = "(]"
    print(isBalanced(expression1))
    print(isBalanced(expression2))