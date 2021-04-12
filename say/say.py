base_nums = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
uniques = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}
num_words = {
    0: [""],
    1: [""],
    2: ["thousand", ""],
    3: ["million", "thousand", ""],
    4: ["billion", "million", "thousand", ""],
}


def say(number):
    if number == 0:
        return "zero"
    if number < 0:
        raise ValueError("Out of range!!")
    if number > 999999999999:
        raise ValueError("Out of range!!")

    result = []
    n = thousand_splitter(number)
    data = filter(lambda group: group[0] != '000', list(zip(n, num_words[len(n)])))
    for d in data:
        result.append(run_digit_convert(d[0]))
        result.append(d[1])

    return " ".join(result).strip()


def run_digit_convert(n: str):
    breakdown = list(zip(hundred_splitter(n), ["hundred", ""]))
    fb = filter(lambda x: int(x[0]) != 0, breakdown)
    result = []
    for num in fb:
        result.append(stringify_number(int(num[0])))
        result.append(num[1])
    return " ".join(result).strip()


def stringify_number(n: int):
    if len(str(n)) == 1:
        return base_nums[n]
    else:
        if str(n)[0] == "1":
            return uniques[int(str(n)[1])]
        else:
            d1 = int(str(n)[0])
            d2 = int(str(n)[1])
            if d2 == 0:
                return f"{tens[d1]}"
            else:
                return f"{tens[d1]}-{base_nums[d2]}"


def thousand_splitter(number: int):
    return f"{number:,}".split(",")


def hundred_splitter(n: str):
    number = n.rjust(3, '0')
    return f"{number[0:1]},{number[1:]}".split(",")
