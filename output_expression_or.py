"""
What will be the output of the python expression True or False?
"""

# evaluating python expression and printing the result
print(True or False)
# or
print("Red" or "White")
# or
print("" or "White")
# or
print(0 or 1)

"""
    result of the above python expression is dependent on the operands of the
    operator because in python non-empty string is always True and 
    empty string is always False.
    
    When the operands of the "Logical operators" are non-bool type then the result
    of the expression will be depends on the either left or right operand.
    
    That's why the result is also become the dependent on the operands of the operator.
    
    In case of logical 'or' operator - 
    
    if the left operand is True, then the result depends on the left operand and 
    that's why the result is the left operand.
    
    whereas the left operand is False, then the result depends on the right operand and
    that's why the result is the right operand.
"""
