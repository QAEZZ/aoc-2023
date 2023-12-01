# == https://adventofcode.com/2023/day/1 ================== #
# The first digit to appear and the last digit to appear    #
# gets concatenated, the result of the concatenation is     #
# the calibration number.                                   #
# ========================================================= #
# Example:                                                  #
# 1abc2 -------> 1 + 2 = 12                                 #
# pqr3stu8vwx -> 3 + 8 = 38                                 #
# a1b2c3d4e5f -> 1 + 5 = 15                                 #
# treb7uchet --> 7 + 7 = 77 | Since there is only one       #
#                           | digit, seven is the           #
#                           | first and last digit.         #
# ========================================================= #

from re import findall

def main() -> int:
    sub_final: list = []

    lines = open('./input.txt', 'r').read().splitlines() # splitlines removes the newline escape seq.
    for line in lines:
        regexed_line = findall(r"\d", line)
        if regexed_line:
            if len(regexed_line) == 1:
                to_append = regexed_line[0] + regexed_line[0]
            else:
                to_append = regexed_line[0] + regexed_line[-1]
            
            sub_final.append(to_append)
    
    calibration_value = sum(map(int, sub_final))
    print(f"Calibration Value: {calibration_value}")
    return calibration_value


def test(calibration_value: int) -> bool:
    if calibration_value != 54990: print('Test failed.'); return

    print('Test passed.')
    return True
            
    

if __name__ == '__main__':
    cv = main()
    test(cv)
