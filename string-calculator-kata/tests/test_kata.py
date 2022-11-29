import unittest

from src.kata import Calculator


class StringCalculatorKata(unittest.TestCase):
    def test_add_method_receives_empty_string(self):
        
        # Arrange
        calculator = Calculator()
        empty_string = ""
        
        # Act
        returned_value = calculator.add(empty_string)
        
        # Assert
        self.assertEqual(returned_value, 0)


    def test_add_method_returns_string_when_receiving_only_one_number(self):
        
        # Arrange
        calculator = Calculator()
        one_number_string = "1"
        
        # Act
        returned_value = calculator.add(one_number_string)
        
        # Assert
        self.assertEqual(returned_value, 1)
        
        
    def test_add_method_returns_sum_if_string_contains_a_colon_and_two_numbers(self):
        
        # Arrange
        calculator = Calculator()
        two_number_string = "1,2"
        
        # Act
        returned_value = calculator.add(two_number_string)
        
        # Assert
        self.assertEqual(returned_value, 3)
