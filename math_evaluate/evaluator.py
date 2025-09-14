def has_operator(tokens: list, op: str) -> bool:
    """Checks whether the list has a particular operator or not"""
    return any(token == op for token in tokens)


def tokenize(expr: str) -> list[int | float | str]:
    """Given an expression, this function will turn it into tokens"""
    try:
        opers = ['+', '-', '*', '/', '^', '(', ')']

        for oper in opers:
            expr = expr.replace(oper, f',{oper},')

        tokens = [token.strip() for token in expr.split(',') if token.strip()]
        
        temp_tokens = []
        for token in tokens:
            if token in opers:
                temp_tokens.append(token)
            elif '.' in token:
                temp_tokens.append(float(token))
            else:
                temp_tokens.append(int(token))

        tokens = temp_tokens

        return tokens
    except ValueError:
        return 'Error: Invalid Characters in expression'


def solve_tokens(tokens: list[int | float | str]) -> str:
    """Solves a tokenized expression (no brackets) following BODMAS/PEMDAS rules."""
    try:
        tokens = tokens.copy()

        if tokens[0] == '-' and tokens[1] != '(':
            temp = str(tokens[1])
            temp = tokens[0] + temp
            if '.' in temp:
                temp = float(temp)
            else:
                temp = int(temp)
            tokens = [temp] + tokens[2:]
        elif '-' in tokens:
            for i in range(len(tokens)-1, 0, -1):
                if tokens[i] == '-' and tokens[i-1] in ['+', '-', '*', '/', '(', '^']:
                    temp = str(tokens[i+1])
                    temp = tokens[i] + temp
                    if '.' in temp:
                        temp = float(temp)
                    else:
                        temp = int(temp)
                    tokens = tokens[:i] + [temp] + tokens[i+2:]
        
        # Exponentiation ^
        while '^' in tokens:
            for i in range(len(tokens)-1, 0, -1):
                if tokens[i] == '^':
                    temp_var = tokens[i-1] ** tokens[i+1]
                    tokens = tokens[:i-1] + [temp_var] + tokens[i+2:]
                    break

        # Division and Multiplication (left to right)
        while has_operator(tokens, '*') or has_operator(tokens, '/'):
            for i, token in enumerate(tokens):
                if token == '*':
                    temp_var = tokens[i-1] * tokens[i+1]
                    tokens = tokens[:i-1] + [temp_var] + tokens[i+2:]
                    break
                elif token == '/':
                    if tokens[i+1] != 0:
                        temp_var = tokens[i-1] / tokens[i+1]
                        tokens = tokens[:i-1] + [temp_var] + tokens[i+2:]
                        break
                    else:
                        return 'Error: Division by zero not possible'

        # Addition and Subtraction (left to right)
        while has_operator(tokens, '+') or has_operator(tokens, '-'):
            for i, token in enumerate(tokens):
                if token == '+':
                    temp_var = tokens[i-1] + tokens[i+1]
                    tokens = tokens[:i-1] + [temp_var] + tokens[i+2:]
                    break
                elif token == '-':
                    temp_var = tokens[i-1] - tokens[i+1]
                    tokens = tokens[:i-1] + [temp_var] + tokens[i+2:]
                    break

        return str(tokens[0])
    except ValueError:
        return 'Error: Invalid Characters in expression'


def solve_brackets(expr: str) -> list | str:
    """Solve brackets in the expression and return tokens or error message"""
    tokens = tokenize(expr)
    
    while '(' in tokens:
        # Find the innermost bracket pair
        start = None
        for i, tok in enumerate(tokens):
            if tok == '(':
                start = i
            elif tok == ')':
                if start is not None:
                    end = i
                    # Extract the content inside the brackets
                    inside = tokens[start+1:end]
                    
                    # Solve the expression inside the brackets
                    solved = solve_tokens(inside)
                    
                    # Check if there was an error
                    if solved.startswith('Error:'):
                        return solved
                    
                    # Convert the string result back to a number
                    try:
                        if '.' in solved:
                            solved_num = float(solved)
                        else:
                            solved_num = int(solved)
                    except ValueError:
                        return f"Error: Could not parse result {solved}"

                    # Replace the bracket expression with the result
                    tokens = tokens[:start] + [solved_num] + tokens[end+1:]
                    break
                else:
                    return "Error: Mismatched closing bracket"
        else:
            # If we get here, we found '(' but no matching ')'
            return "Error: Mismatched opening bracket"
    
    return tokens


def solve(tokens: list) -> str:
    """Takes tokens as input and returns the mathematically evaluated result"""
    return solve_tokens(tokens)


def evaluate(expr: str) -> str:
    """Takes an expression as input and returns the mathematically evaluated result or error message"""
    # First solve all brackets
    tokens_solved_brackets = solve_brackets(expr)
    
    # Check if bracket solving returned an error
    if isinstance(tokens_solved_brackets, str):
        return tokens_solved_brackets
    
    # Now solve the remaining expression
    result = solve(tokens_solved_brackets)
    return result
