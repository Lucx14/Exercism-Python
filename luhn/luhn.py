class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num.replace(" ", "")

    def valid(self) -> bool:
        return (
            len(self.card_num) > 1
            and all(map(str.isdigit, self.card_num))
            and self.valid_luhn()
        )

    def valid_luhn(self):
        nums = self.card_digits()[::-1]
        for i in range(1, len(nums), 2):
            nums[i] *= 2
            if nums[i] > 9:
                nums[i] -= 9

        return sum(nums) % 10 == 0

    def card_digits(self):
        return [int(char) for char in self.card_num]
