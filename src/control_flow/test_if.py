"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'The number is positive or zero'

    assert conclusion == 'The number is positive or zero'

def test_grade_classification():
    """Test grade classification using multiple elif conditions."""

    grade = 85
    result = ""

    if grade >= 90:
        result = "A"
    elif grade >= 80:
        result = "B"
    elif grade >= 70:
        result = "C"
    elif grade >= 60:
        result = "D"
    else:
        result = "F"
    assert result == "B"


def test_nested_conditions():
    """Test nested if statements."""

    age = 20
    completed_prerequisite = True
    result = ""

    if age >= 18:
        if completed_prerequisite:
            result = "Eligible"
        else:
            result = "Prerequisite required"
    else:
        result = "Not eligible due to age"

    assert result == "Eligible"    
    
