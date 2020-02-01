# day 3

# practice to transform 12345 into 54321
# my answer

number = int(input('Please enter the number:'))
b = len(str(number))
result = 0
for i in range(b):
    get_number = ( number // (10 ** i) ) % 10
    result += get_number * (10 ** (b - i - 1))
print(result)


# case answer
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    #print(reversed_num)
    num //= 10
    #print(num)
print(reversed_num)
