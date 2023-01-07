"""
What will be the output of the python expression "Red" and "White"?
"""

# evaluating expression and printing the result
print(True and False)
# or
print("Red" and "White")
# or
print("" and "white")
# or
print(0 and 1)

"""
    result of the above python expression is dependent on the operands of the
    operator because in python non-empty string is always True and 
    empty string is always False.
    
    When the operands of the "Logical operators" are non-bool type then the result
    of the expression will be depends on the either left or right operand.
    
    That's why the result is also become the dependent on the operands of the operator.
    
    In case of logical 'and' operator - 
    
    if the left operand is True, then the result depends on the right operand and 
    that's why the result is the right operand.
    
    whereas the left operand is False, then the result depends on the left operand and
    that's why the result is the left operand.
"""