# Program to check whether parentheses are balanced or not
# Using Stack
 
def is_balanced(exp):
    stack = []
    for char in exp:
 
        # If opening bracket, push into stack
        if char in "({[":
            stack.append(char)
 
        # If closing bracket
        else:
            # If stack becomes empty
            # no opening bracket is available
            if not stack:
                return False
 
            # Remove top element from stack
            top = stack.pop()
 
            # Check matching brackets
 
            # ) should match (
            if char == ')' and top != '(':
                return False
 
            # } should match {
            if char == '}' and top != '{':
                return False
 
            # ] should match [
            if char == ']' and top != '[':
                return False
 
    # If stack becomes empty
    # all brackets are balanced
    return len(stack) == 0

exp = "{[(])}"
 
if is_balanced(exp):
    print("Parentheses are Balanced")
else:
    print("Parentheses are NOT Balanced")
