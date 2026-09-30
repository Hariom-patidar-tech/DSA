# Stack Implementation
# Valid Parentheses                                   =                       Complete
# Reverse String using Stack
# Next Greater Element
# Stock Span Problem
# Daily Temperatures
# Min Stack
# Largest Rectangle in Histogram
# Infix to Postfix
# Evaluate Postfix Expression


def valid_parentheses(s):

    stack = []

    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:

        if ch in "({[":
            stack.append(ch)

        else:
            if not stack:
                return False

            top = stack.pop()

            if top != brackets[ch]:
                return False

    return len(stack) == 0


s = input("Enter Parentheses: ")

if valid_parentheses(s):
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")