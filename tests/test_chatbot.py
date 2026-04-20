"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

import unittest
from unittest import TestCase, main
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import MagicMock
from src.chatbot import ACCOUNTS, VALID_TASKS, get_account_number, get_amount, get_balance, get_task, make_deposit

__author__ = "Lichao Huang"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Faculty"

class TestFunction(unittest.TestCase):
    def test_get_account_number_type_error(self):
        with patch('builtins.input') as mock_input:
        # Arrange
            mock_input.side_effect = ["non_numeric_data"]
            with self.assertRaises(TypeError) as context:
                get_account_number()
        expected = "Account number must be an int type."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_get_account_number_value_error(self):
        with patch('builtins.input') as mock_input:
        # Arrange
            mock_input.side_effect = ["112233"]
            with self.assertRaises(ValueError) as context:
                get_account_number()
        expected = "Account number entered does not exist."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_get_account_number_no_error(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["123456"]
            expected = 123456
            # Act
            actual = get_account_number()
            self.assertEqual(expected, actual)

    def test_get_amount_value_error_0(self):
        # Arrange
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["0"]
            with self.assertRaises(ValueError) as context:
                get_amount()
        expected = "Amount must be a value greater than zero."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_get_amount_value_error_negative(self):
        # Arrange
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["-1"]
            with self.assertRaises(ValueError) as context:
                get_amount()
        expected = "Amount must be a value greater than zero."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)
    
    def test_get_amount_type_error(self):
        # Arrange
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["a"]
            with self.assertRaises(TypeError) as context:
                get_amount()
        expected = "Amount must be a numeric type."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_get_amount_no_error(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["100"]
            expected = 100
            # Act
            actual = get_amount()
            self.assertEqual(expected, actual)
    
    def test_get_balance_not_int(self):
        with patch('builtins.input') as mock_input:
        # Arrange
            mock_input.side_effect = ["1.1"]
            with self.assertRaises(TypeError) as context:
                get_account_number()
        expected = "Account number must be an int type."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)
    
    def test_get_balance_account_not_found(self):
        with patch('builtins.input') as mock_input:
        # Arrange
            mock_input.side_effect = ["112233"]
            with self.assertRaises(ValueError) as context:
                get_account_number()
        expected = "Account number entered does not exist."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_make_deposit_number_not_int(self):
        with patch('builtins.input') as mock_input:
        # Arrange
            mock_input.side_effect = ["1.1"]
            with self.assertRaises(TypeError) as context:
                get_account_number()
        expected = "Account number must be an int type."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_make_deposit_not_valid_account(self):
        with patch('builtins.input') as mock_input:
        # Arrange
            mock_input.side_effect = ["112233"]
            with self.assertRaises(ValueError) as context:
                get_account_number()
        expected = "Account number entered does not exist."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_make_deposit_not_number(self):
        with patch('builtins.input') as mock_input:
        # Arrange
            mock_input.side_effect = ["aaa"]
            with self.assertRaises(TypeError) as context:
                get_account_number()
        expected = "Account number must be an int type."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_make_deposit_negetive(self):
        # Arrange
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["-1"]
            with self.assertRaises(ValueError) as context:
                get_amount()
        expected = "Amount must be a value greater than zero."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_make_deposit_0(self):
        # Arrange
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["0"]
            with self.assertRaises(ValueError) as context:
                get_amount()
        expected = "Amount must be a value greater than zero."
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_get_task_upper(self):
        with patch('builtins.input') as mock_input:
        # Arrange
            mock_input.side_effect = ["Deposit"]
            expected = "deposit"
        # Act
            actual = get_task()
            self.assertEqual(expected, actual)

    def test_get_task_unknow_task(self):
        # Arrange
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["Dep"]
            with self.assertRaises(ValueError) as context:
                get_task()
        expected = "unknown task"
        # Act
        actual = str(context.exception)
        self.assertEqual(expected, actual)        


'''
    def test_get_balance():
        # Arrange
        # Act
        # Assert
    def test_make_deposit():
        # Arrange
        # Act
        # Assert
    def test_get_task():
        # Arrange
        # Act
        # Assert
'''