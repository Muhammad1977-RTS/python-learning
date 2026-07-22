num = int(input())
original_num = num
sum_of_digits = 0
count_of_digits = 0
product_of_digits = 1

for i in range(len(str(num))):
    digit = num % 10
    sum_of_digits += digit
    count_of_digits += 1
    product_of_digits *= digit
    average = sum_of_digits / count_of_digits
    num //= 10

    first_digit = original_num // (10 ** (count_of_digits - 1))
    last_digit = original_num % 10
    sum_digits = first_digit + last_digit
print(sum_of_digits)
print(count_of_digits)
print(product_of_digits)
print(average)
print(first_digit)
print(sum_digits)
