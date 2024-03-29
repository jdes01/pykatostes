import unittest

import pytest

from src.kata import Calculator, NegativeNumberException


class StringCalculatorKata(unittest.TestCase):
    def test_add_method_receives_empty_string(self):
        
        # Arrange
        empty_string = ""
        
        # Act
        returned_value = Calculator.add(empty_string)
        
        # Assert
        self.assertEqual(returned_value, 0)


    def test_add_method_returns_string_when_receiving_only_one_number(self):
        
        # Arrange
        one_number_string = "1"
        
        # Act
        returned_value = Calculator.add(one_number_string)
        
        # Assert
        self.assertEqual(returned_value, 1)
        
        
    def test_add_method_returns_sum_if_string_contains_a_colon_and_two_numbers(self):
        
        # Arrange
        two_number_string = "1,2"
        
        # Act
        returned_value = Calculator.add(two_number_string)
        
        # Assert
        self.assertEqual(returned_value, 3)

    def test_add_method_returns_sum_if_string_contains_more_than_a_number(self):
        
        # Arrange
        two_number_string = "1,2,3,4,5"
        
        # Act
        returned_value = Calculator.add(two_number_string)
        
        # Assert
        self.assertEqual(returned_value, 15)
        
        
    def test_add_method_returns_sum_if_string_contains_line_jump(self):
        
        # Arrange
        two_number_string = "1\n,2,\n3"
        
        # Act
        returned_value = Calculator.add(two_number_string)
        
        # Assert
        self.assertEqual(returned_value, 6)
        
    def test_add_method_returns_sum_if_string_contains_new_line_delimeter(self):
        
        # Arrange
        two_number_string = "//a\n1a2a3"
        
        # Act
        returned_value = Calculator.add(two_number_string)
        
        # Assert
        self.assertEqual(returned_value, 6)

    def test_negative_numbers_are_not_allowed(self):
        
        # Arrange
        negative_numbers_string = "-1,2"

        # Act
        with pytest.raises(NegativeNumberException) as e:
            Calculator.add(negative_numbers_string)
            
        # Assert
        assert "Negative numbers found: [-1]" in str(e.value)

    def test_returned_message_when_adding_multiple_negative_numbers(self):
        
        # Arrange
        negative_numbers_string = "-1,-2,-3"

        # Act
        with pytest.raises(NegativeNumberException) as e:
            Calculator.add(negative_numbers_string)
            
        # Assert
        assert "Negative numbers found: [-1, -2, -3]" in str(e.value)
