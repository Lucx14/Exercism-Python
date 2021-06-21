INPUT_ERROR = "Error: Invalid phone number"


class PhoneNumber:
    def __init__(self, number):
        self.number = PhoneNumber.extract_nanp_numbers(number)
        self.validate_number()
        self.area_code = self.number[:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"

    def validate_number(self):
        if self.invalid_area_code() or self.invalid_exchange_code():
            raise ValueError(INPUT_ERROR)

    def invalid_area_code(self):
        return self.number[0] in ("1", "0")

    def invalid_exchange_code(self):
        return self.number[3] in ("1", "0")

    @staticmethod
    def extract_nanp_numbers(number: str) -> str:
        numbers = list(filter(str.isdigit, number))
        if len(numbers) not in (10, 11) or (len(numbers) == 11 and numbers[0] != "1"):
            raise ValueError(INPUT_ERROR)
        if len(numbers) == 11 and numbers[0] == "1":
            numbers.pop(0)
        return "".join(numbers)
