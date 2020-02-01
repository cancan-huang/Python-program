# day 3

# practice to transform 12345 into 54321

number = int(input('Please enter the number:'))
b = len(str(number))
result = 0
for i in range(b):
    get_number = ( number // (10 ** i) ) % 10
    result += get_number * (10 ** (b - i - 1))
print(result)
