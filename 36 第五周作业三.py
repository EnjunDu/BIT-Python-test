def multiply_numbers(*args):
    result =1
    for num in args:
        result *= num
    return result
input_str = input("")
numbers = [int(num) for num in input_str.split(',')]
result = multiply_numbers(*numbers)
print( result)
