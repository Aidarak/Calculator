# calculator.py
# ARYAN KARADIA, ENDG 233 F21

first_val = int(input('Enter the first value: ')) # Gets input from user for first value
first_op = str(input('Enter the first Operator: ')) # Gets input from user for first operator
second_val = int(input('Enter the second value: ')) # Gets input from user for second value
second_op = str(input('Enter the second operator: ')) # Gets input from user for second operator
third_val = int(input('Enter the third value: ')) # Gets input from user for third value

if first_op == '*': # if the first operator is multiplication, multiply the first two values
    intermediate_value = first_val * second_val
    if second_op == '*': # if the second operator is multiplication, multiply the intermediate value by the third input value
        answer = intermediate_value * third_val
    elif second_op == '/': # if the second operator is division, divide the intermediate value by the third input value
        answer = intermediate_value // third_val
    elif second_op == '+': # if the second operator is addition, add the imtermediate value with the third input value
        answer = intermediate_value + third_val
    elif second_op == '-': # if the second operator is subtract, subtract the third input value from the intermediate value
        answer = intermediate_value - third_val
elif first_op == '/': # if the first operator is division, divide the first two values
    intermediate_value = first_val // second_val
    if second_op == '*': # if the second operator is multiplication, multiply the intermediate value by the third input value
        answer = intermediate_value * third_val
    elif second_op == '/': # if the second operator is division, divide the intermediate value by the third input value
        answer = intermediate_value // third_val
    elif second_op == '+': # if the second operator is addition, add the intermediate value and the third input value
        answer = intermediate_value + third_val
    elif second_op == '-': # if the second operator is subtract, subtract the third input value from the intermediate value
        answer = intermediate_value - third_val
elif second_op == '*': # if the first operator was not multiplication and the second operator is multiplication, multiply the second input value by the third input value
    intermediate_value = second_val * third_val
    if first_op == '+': # if the first operator is addition, add the first input value with the intermediate value
        answer = first_val + intermediate_value
    elif first_op == '-': # if the first operator is subtraction, subtract the intermediate value from the first input value
        answer = first_val - intermediate_value
elif second_op == '/': # if the first operator isn't multiplication or division and the second operator is divison, divide the second input value by the third input value
    intermediate_value = second_val // third_val
    if first_op == '+': # if the first operator is addition, add the first input value and the intermediate value
        answer = first_val + intermediate_value
    elif first_op == '-': # if the first operator is subtraction, subtract the intermediate value from the first input value
        answer = first_val - intermediate_value
elif first_op == '+': # if both operators are not multiplication or division and the first operator is addition, add the first input value and the second input value
    intermediate_value = first_val + second_val
    if second_op == '+': # if the second operator is addition, add the intermediate value with the third input value
        answer = intermediate_value + third_val
    elif second_op == '-': # if the second operator is subtraction, subtract the third input value from the intermediate value
        answer = intermediate_value - third_val
elif first_op == '-': # if both operators are not multiplication or division and the first operator is subtraction, subtract the second input value from the first input value
    intermediate_value = first_val - second_val
    if second_op == '+': # if the second operator is addition, add the intermediate value and the third input value
        answer = intermediate_value + third_val
    elif second_op == '-': # if the second operator is subtraction, subtract the third input value by the intermediate value
        answer = intermediate_value - third_val

print('Entered expression:', first_val, first_op, second_val, second_op, third_val) # prints out the entered expression
print(f'Your final answer = {answer:.0f}') # prints out final answer
