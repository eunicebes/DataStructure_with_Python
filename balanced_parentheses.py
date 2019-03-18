import sys

def isVaild(input_string):
    stack = []
    mapping = {"(": ")", "[": "]", "{": "}"}

    for char in input_string:
        if char in mapping:
            stack.append(char)
        elif len(stack) != 0 and mapping[stack[-1]] == char:
            stack.pop()
        else:
            return False

    return stack == []

input_str = input("Enter a parentheses sequence: ")
print(isVaild(input_str))