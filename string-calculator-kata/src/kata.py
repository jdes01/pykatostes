from typing import Optional, Union

def is_true():
    return True

class Calculator():
    def __init__(self):
        pass
    
    def add(self, string: str) -> int:
        if string == "":
            return 0
        
        if "," in string:
            return self.__split_string_and_sum(string)
        
        return int(string)
    
    def __split_string_and_sum(self, string: str) -> int:
        possible_numbers = "1234567890"
        numbers = string.split(",")
        
        if len(numbers) != 2:
            raise Exception("More than two numbers exception")
        
        if numbers[0] not in possible_numbers:
            raise Exception("Not a number")
        
        if numbers[1] not in possible_numbers:
            raise Exception("Not a number")
        
        return int(numbers[0]) + int(numbers[1])