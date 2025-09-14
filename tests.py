import unittest
from math_evaluate.evaluator import evaluate, tokenize, solve_tokens, solve_brackets


class TestTokenizer(unittest.TestCase):
    """Test the tokenize function"""
    
    def test_basic_tokenization(self):
        result = tokenize("5+3")
        expected = [5, '+', 3]
        self.assertEqual(result, expected)
    
    def test_tokenization_with_spaces(self):
        result = tokenize("5 + 3")
        expected = [5, '+', 3]
        self.assertEqual(result, expected)
    
    def test_tokenization_with_floats(self):
        result = tokenize("3.14+2.5")
        expected = [3.14, '+', 2.5]
        self.assertEqual(result, expected)
    
    def test_tokenization_with_brackets(self):
        result = tokenize("(5+3)*2")
        expected = ['(', 5, '+', 3, ')', '*', 2]
        self.assertEqual(result, expected)
    
    def test_tokenization_with_all_operators(self):
        result = tokenize("1+2-3*4/5^6")
        expected = [1, '+', 2, '-', 3, '*', 4, '/', 5, '^', 6]
        self.assertEqual(result, expected)


class TestBasicArithmetic(unittest.TestCase):
    """Test basic arithmetic operations"""
    
    def test_addition(self):
        self.assertEqual(evaluate("5+3"), "8")
        self.assertEqual(evaluate("0+0"), "0")
        self.assertEqual(evaluate("10+20"), "30")
    
    def test_subtraction(self):
        self.assertEqual(evaluate("5-3"), "2")
        self.assertEqual(evaluate("10-20"), "-10")
        self.assertEqual(evaluate("0-5"), "-5")
    
    def test_multiplication(self):
        self.assertEqual(evaluate("5*3"), "15")
        self.assertEqual(evaluate("0*100"), "0")
        self.assertEqual(evaluate("7*8"), "56")
    
    def test_division(self):
        self.assertEqual(evaluate("15/3"), "5.0")
        self.assertEqual(evaluate("7/2"), "3.5")
        self.assertEqual(evaluate("100/4"), "25.0")
    
    def test_exponentiation(self):
        self.assertEqual(evaluate("2^3"), "8")
        self.assertEqual(evaluate("5^2"), "25")
        self.assertEqual(evaluate("3^0"), "1")


class TestOrderOfOperations(unittest.TestCase):
    """Test BODMAS/PEMDAS order of operations"""
    
    def test_multiplication_before_addition(self):
        self.assertEqual(evaluate("2+3*4"), "14")  # Not 20
        self.assertEqual(evaluate("5*2+3"), "13")  # Not 25
    
    def test_division_before_subtraction(self):
        self.assertEqual(evaluate("10-6/2"), "7.0")  # Not 2
        self.assertEqual(evaluate("8/4-1"), "1.0")   # Not 2
    
    def test_exponentiation_before_multiplication(self):
        self.assertEqual(evaluate("2*3^2"), "18")    # Not 36
        self.assertEqual(evaluate("3^2*2"), "18")    # Same result
    
    def test_left_to_right_same_precedence(self):
        self.assertEqual(evaluate("8/4/2"), "1.0")   # Left to right: (8/4)/2
        self.assertEqual(evaluate("10-5-2"), "3")    # Left to right: (10-5)-2
        self.assertEqual(evaluate("2*3*4"), "24")    # Left to right: (2*3)*4


class TestBrackets(unittest.TestCase):
    """Test bracket handling"""
    
    def test_simple_brackets(self):
        self.assertEqual(evaluate("(5+3)"), "8")
        self.assertEqual(evaluate("(10-5)*2"), "10")
        self.assertEqual(evaluate("3*(2+4)"), "18")
    
    def test_nested_brackets(self):
        self.assertEqual(evaluate("((5+3)*2)"), "16")
        self.assertEqual(evaluate("(2*(3+4))"), "14")
        self.assertEqual(evaluate("((2+3)*(4+5))"), "45")
    
    def test_multiple_bracket_pairs(self):
        self.assertEqual(evaluate("(5+3)*(2+1)"), "24")
        self.assertEqual(evaluate("(10/2)+(3*4)"), "17.0")
    
    def test_complex_nested_expression(self):
        self.assertEqual(evaluate("(3*(9+0))-9*(2+3)"), "-18")


class TestUnaryMinus(unittest.TestCase):
    """Test unary minus operator"""
    
    def test_unary_minus_at_start(self):
        self.assertEqual(evaluate("-5"), "-5")
        self.assertEqual(evaluate("-10"), "-10")
        self.assertEqual(evaluate("-3.14"), "-3.14")
    
    def test_unary_minus_after_operators(self):
        self.assertEqual(evaluate("5+-3"), "2")     # 5 + (-3)
        self.assertEqual(evaluate("5--3"), "8")     # 5 - (-3)
        self.assertEqual(evaluate("2*-3"), "-6")    # 2 * (-3)
        self.assertEqual(evaluate("10/-2"), "-5.0") # 10 / (-2)
    
    def test_unary_minus_after_brackets(self):
        self.assertEqual(evaluate("(5)+-3"), "2")   # Should be 5 + (-3)
        self.assertEqual(evaluate("(2)*-4"), "-8")  # Should be 2 * (-4)
    
    def test_multiple_unary_minus(self):
        self.assertEqual(evaluate("--5"), "5")      # -(-5) = 5
        self.assertEqual(evaluate("5*-3+-2"), "-17") # 5*(-3) + (-2)


class TestFloatNumbers(unittest.TestCase):
    """Test floating point number handling"""
    
    def test_float_arithmetic(self):
        self.assertEqual(evaluate("3.5+2.5"), "6.0")
        self.assertEqual(evaluate("7.5-2.5"), "5.0")
        self.assertEqual(evaluate("2.5*4"), "10.0")
        self.assertEqual(evaluate("7.5/2.5"), "3.0")
    
    def test_mixed_int_float(self):
        self.assertEqual(evaluate("5+3.5"), "8.5")
        self.assertEqual(evaluate("10-2.5"), "7.5")


class TestErrorCases(unittest.TestCase):
    """Test error handling"""
    
    def test_division_by_zero(self):
        self.assertEqual(evaluate("5/0"), "Error: Division by zero not possible")
        self.assertEqual(evaluate("10/0"), "Error: Division by zero not possible")
    
    def test_division_by_zero_in_expression(self):
        self.assertEqual(evaluate("5+10/0"), "Error: Division by zero not possible")
        self.assertEqual(evaluate("(3+2)/0*4"), "Error: Division by zero not possible")


class TestComplexExpressions(unittest.TestCase):
    """Test complex mathematical expressions"""
    
    def test_complex_bodmas(self):
        self.assertEqual(evaluate("2+3*4-5/5^2"), "13.8")  # 2+12-5/25 = 2+12-0.2
        self.assertEqual(evaluate("3*9+0-9*2+3"), "12")    # 27+0-18+3
    
    def test_complex_with_brackets_and_unary(self):
        self.assertEqual(evaluate("-(2+3)*4"), "-20")      # -(5)*4
        self.assertEqual(evaluate("-2*(3+4)"), "-14")      # -2*7
        self.assertEqual(evaluate("(-2+5)*3"), "9")        # 3*3
    
    def test_deeply_nested(self):
        self.assertEqual(evaluate("((2+3)*(4+1))"), "25")  # (5*5)
        self.assertEqual(evaluate("(((1+2)*3)+4)"), "13")  # ((3*3)+4) = (9+4)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""
    
    def test_single_number(self):
        self.assertEqual(evaluate("42"), "42")
        self.assertEqual(evaluate("3.14"), "3.14")
    
    def test_single_negative_number(self):
        self.assertEqual(evaluate("-42"), "-42")
        self.assertEqual(evaluate("-3.14"), "-3.14")
    
    def test_zero_operations(self):
        self.assertEqual(evaluate("0+5"), "5")
        self.assertEqual(evaluate("5-0"), "5")
        self.assertEqual(evaluate("0*100"), "0")
        self.assertEqual(evaluate("0^5"), "0")
    
    def test_power_of_zero_and_one(self):
        self.assertEqual(evaluate("5^0"), "1")  # Any number to power 0 is 1
        self.assertEqual(evaluate("5^1"), "5")  # Any number to power 1 is itself


if __name__ == '__main__':
    # Run all tests
    unittest.main(verbosity=2)