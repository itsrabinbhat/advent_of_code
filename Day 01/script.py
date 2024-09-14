import re
# Reading data from data file
with open('data.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

total_sum = 0
word_digit = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def extract_digits_and_combine(line):
    # digits = re.findall(r'\d', line)  # Find all digits in the line
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))' 
    digits = re.findall(pattern, line)
    if len(digits) == 0:
        return None  
    elif len(digits) == 1:
        if digits[0] in word_digit:
            new_digit = word_digit[digits[0]]
            return new_digit * 2
        
        return digits[0] * 2  
    else:
        f_digit = digits[0]
        l_digit = digits[-1]
        if f_digit in word_digit:
            f_digit = word_digit[f_digit]

        if l_digit in word_digit:
            l_digit = word_digit[l_digit]
        return f_digit + l_digit 
    
for line in lines:
    num = extract_digits_and_combine(line)
    print(line,"->", num)
    if num != None:
        total_sum += int(num)

print(total_sum)