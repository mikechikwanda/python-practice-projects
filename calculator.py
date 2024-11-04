import math

# Dictionary of allowed functions and constants for safe evaluation
safe_dict = {
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "pow": pow,
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
}


def calculator():
    """
    Runs a safe calculator that accepts mathematical expressions as input
    and evaluates them using a restricted set of functions and constants.

    Allowed functions:
        abs, round, min, max, pow, sqrt, sin, cos, tan, log, exp
    Constants:
        pi, e

    Syntax Guide:
        Enter mathematical expressions like 'sqrt(16)' or 'sin(pi/2)'.
        Enter 'q' to quit the calculator.
    """
    while True:
        # Prompt the user to enter an expression or 'q' to quit
        expression = input("Enter expression or 'q' to quit: ").strip()

        if expression.lower() == "q":
            print("Calculator exited")
            break

        try:
            # Evaluate the expression using only the functions and constants in safe_dict
            answer = eval(expression, {"__builtins__": None}, safe_dict)
            print("Result:", answer)
        except Exception as e:
            print("Error:", e)


# Run the calculator
calculator()
