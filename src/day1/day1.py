# == https://adventofcode.com/2023/day/1 ================== #
# The first digit to appear and the last digit to appear    #
# gets concatenated, the sum of the all concatenated is the #
# calibration number.                                       #
# ========================================================= #
# Part One                                                  #
# ========================================================= #
# Example:                                                  #
# 1abc2 --------> 1 + 2 = 12                                #
# pqr3stu8vwx --> 3 + 8 = 38                                #
# a1b2c3d4e5f --> 1 + 5 = 15                                #
# treb7uchet ---> 7 + 7 = 77 | Since there is only one      #
#                            | digit, seven is the          #
#                            | first and last digit.        #
# ========================================================= #
# Part Two                                                  #
# ========================================================= #
# Little different for part two, same concept as part one   #
# however, we must also take into account that the digits   #
# can be in word form. i.e. one, two, seven, etc.           #
#                                                           #
# With that in mind, the website says that it only uses one #
# through nine. No need to worry about digits > 9 nor < 1.  #
#                                                           #
# Example:                                                  #
# two1nine -----> two + nine = 29                           #
# eightwothree -> eight + three = 83                        #
# abone2threex -> one + 2 + three = 123                     #
# 7pqtsixteen --> 7 + six = 76                              #
# ========================================================= #

import regex as re # pip3 install regex

def get_lines() -> list[str]: return open('./input.txt', 'r').read().splitlines() # splitlines removes the newline escape seq.
def get_int_sum(lst: list) -> int: return sum(map(int, lst))


class PartOne:
    def find_calibration_value() -> int:
        sub_final: list = []

        lines = get_lines()
        for line in lines:
            regexed_line = re.findall(r'\d', line)
            if regexed_line:
                if len(regexed_line) == 1:
                    to_append = regexed_line[0] + regexed_line[0]
                else:
                    to_append = regexed_line[0] + regexed_line[-1]
                
                sub_final.append(to_append)

        return get_int_sum(sub_final)


    def test(calibration_value: int) -> bool:
        if calibration_value != 54990: return False
        return True           


class PartTwo:
    def find_calibration_value() -> int:
        sub_final: list = []

        conversion_dict = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
        }

        pattern = re.compile(r'(' + '|'.join(conversion_dict.keys()) + r'|\d)')
        lines = get_lines()
        
        for line in lines:
            matches = pattern.findall(line, overlapped=True)
            regexed_line = [conversion_dict[match] if match in conversion_dict else int(match) for match in matches] # if it's a word, convert the match to ints using the dict
            if regexed_line:
                if len(regexed_line) == 1:
                    to_append = str(regexed_line[0]) + str(regexed_line[0])
                else:
                    to_append = str(regexed_line[0]) + str(regexed_line[-1])
                
                sub_final.append(to_append)

        return get_int_sum(sub_final)
    
    def test(calibration_value: int) -> bool:
        if calibration_value != 54473: return False
        return True



if __name__ == '__main__':
    print('Part one...')
    part1_cv = PartOne.find_calibration_value()
    print(f"Calibration Value: {part1_cv} | Test {'passed' if PartOne.test(part1_cv) else 'failed, incorrect value'}.")

    print('\nPart two...')
    part2_cv = PartTwo.find_calibration_value()
    print(f"Calibration Value: {part2_cv} | Test {'passed' if PartTwo.test(part2_cv) else 'failed, incorrect value'}.")

