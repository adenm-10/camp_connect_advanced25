"""Logical Operators"""
a, b, c = True, False, True

# AND: Both conditions must be True
if a and c:
    print("Both a and c are True (AND condition).")

# OR: At least one condition must be True
if b or c:
    print("Either b or c is True (OR condition).")

# NOT: Reverses the condition
if not b:
    print("b is False (NOT condition).")