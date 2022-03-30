def arithmetic_arranger(problems,val:False):
    
    
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems"
        return arranged_problems
    
    operations = list(map(lambda x: x.split()[1], problems))
    if set(operations) != {'+', '-'} and len(set(operations)) != 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems

    numbers = []
    for x in problems:
        n = x.split()
        numbers.extend([n[0],n[2]])
    
    for x in numbers:
        if not x.isdigit():
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems

    for x in numbers:
        if len(x) > 5:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems
 
    values =  []
    for x in problems:
        values.append(eval(x))
    
    top_row = ''
    dashes = ''
    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
        top_row += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    bottom_row = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_row += operations[i // 2]
        bottom_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_row += ' ' * 4

    if val:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))
    return arranged_problems



