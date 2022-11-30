import re

class Calculator():
    
    @staticmethod
    def add(string: str) -> int:

        if string == "":
            return 0
        
        if "\n" in string:
            string = string.replace("\n", "")
        
        if re.search("^//.{1}", string):
            string = string.replace("//", "")
            new_delimeter = string[0]
            string = string[1:]
            string = string.replace(new_delimeter, ",")
            
        if "," not in string:
            return int(string)

        numbers = [int(number) for number in string.split(",")]

        return sum(numbers)
