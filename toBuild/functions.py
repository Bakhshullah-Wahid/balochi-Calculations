import keywords as k
import separation as s

def toOperate(value, value2, value3):
    v = None
    digit = []
    if value2 == '+':
        v = value + value3
        if v > 20:
            digit.append(v // 10)
            digit.append(v % 10)
           
            return digit
        else:
            digit.append(v)
            return digit
    elif value2 == '-':
        v = value - value3
        if v > 20:
            digit.append(v // 10)
            digit.append(v % 10)
           
            return digit
    elif value2 == '*':
        v = value * value3
       
        if v > 20:
            digit = s.change(v)
           
            return digit
        else:
            digit.append(v)
            return digit

input_string = "BEESTH JAMA SAY".split()
tokens = []
for word in input_string:
    if word in k.NUMBERS:
        tokens.append(['NUMBERS', k.NUMBERS[word]])
    elif word in k.ARETHMATIC:
        tokens.append(['OPERATOR', k.ARETHMATIC[word]])

print(tokens)

result_list = toOperate(tokens[0][1], tokens[1][1], tokens[2][1])
print(result_list)

result = ''

for num in result_list:
    for key, value in k.NUMBERS.items():
        if value == num:
            result += key

print(result)
