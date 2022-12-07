import re

class NegativeNumberException(Exception):
    pass

class Calculator():

    @staticmethod
    def add(input: str) -> int:

        if input == "":
            return 0

        input = Calculator.remove_line_breaks(input)

        if re.search("^//.{1}", input):
            input = Calculator.change_delimeter(input)

        if "," not in input:
            return int(input)

        numbers = Calculator.extract_numbers_from_string(input)
        
        negative_numbers: list[int] = list(filter(lambda number: number < 0, numbers))
        if negative_numbers: 
            raise NegativeNumberException("Negative numbers found: {}".format(negative_numbers))

        return sum(numbers)

    def remove_line_breaks(input: str) -> str:
        if "\n" in input:
            input = input.replace("\n", "")

        return input

    def change_delimeter(input: str) -> str:
        input = input.replace("//", "")
        new_delimeter = input[0]
        input = input[1:]
        return input.replace(new_delimeter, ",")

    def extract_numbers_from_string(input: str) -> list[int]:
        return [int(number) for number in input.split(",")]