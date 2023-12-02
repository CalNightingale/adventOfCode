test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

test_two = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

digits = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
        }

def process_line(line: str):
    min_index = None
    min_digit = None
    max_index = None
    max_digit = None
    for digit in list(digits.keys()) + list(digits.values()):
        try:
            index = line.index(digit)
            if min_index == None or index < min_index:
                min_digit = digit
                min_index = index
            l_index = line.rindex(digit)
            if max_index == None or l_index > max_index:
                max_index = l_index
                max_digit = digit
        except:
            continue

    if min_digit == None or max_digit == None:
        return 0
    return int(digits.get(min_digit, min_digit) + digits.get(max_digit, max_digit))

def read_file():
    with open("input.txt") as f:
        data = f.read()
    return data.split('\n')

def part1():
    lines = read_file()
    sum = 0
    for line in lines:
        processed = process_line(line)
        sum += processed
    print(sum)


if __name__ == "__main__":
    part1()

