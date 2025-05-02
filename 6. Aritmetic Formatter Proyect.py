def arithmetic_arranger(problems, show_answers=False):
    # Error check for number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Initialize lists for parts of each row
    top_row = []
    bottom_row = []
    dashes = []
    answers = []

    # Process each problem
    for problem in problems:
        # Split the problem into elements
        num1, operator, num2 = problem.split()
        
        # Error checks
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine spacing
        space_width = max(len(num1), len(num2)) + 2

        # Prepare rows
        top_row.append(num1.rjust(space_width))
        bottom_row.append(operator + ' ' + num2.rjust(space_width - 2))
        dashes.append('-' * space_width)

        # Calculate answer if needed
        if show_answers:
            result = str(int(num1) + int(num2)) if operator == '+' else str(int(num1) - int(num2))
            answers.append(result.rjust(space_width))

    # Join rows with 4 spaces between each problem
    top_row_str = '    '.join(top_row)
    bottom_row_str = '    '.join(bottom_row)
    dashes_str = '    '.join(dashes)
    
    if show_answers:
        answer_row_str = '    '.join(answers)
        arranged_problems = '\n'.join((top_row_str, bottom_row_str, dashes_str, answer_row_str))
    else:
        arranged_problems = '\n'.join((top_row_str, bottom_row_str, dashes_str))
    
    return arranged_problems

# Test example
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
